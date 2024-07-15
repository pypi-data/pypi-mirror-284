from functools import wraps
from json import loads, JSONDecodeError
from typing import Callable, Dict, Literal, Optional, Tuple, TypeVar, Any
import asyncio

from d42 import validate_or_fail
from schemax_openapi import SchemaData
from jj import RelayResponse
from .utils import load_cache, normalize_path
from revolt.errors import SubstitutionError
from valera import ValidationException

_T = TypeVar('_T')


class Validator:
    @staticmethod
    def _check_entity_match(entity_dict: Dict[Tuple[str, str], SchemaData],
                            http_method: str,
                            path: str) -> Optional[SchemaData]:
        normalized_path = normalize_path(path)
        entity_key = (http_method.lower(), normalized_path)
        return entity_dict.get(entity_key)

    @staticmethod
    def _handle_non_strict_validation_error(parsed_request: Optional[SchemaData],
                                            decoded_mocked_body: Any,
                                            validate_level: Literal["error", "warning", "skip"],
                                            func_name: str) -> None:

        try:
            parsed_request.response_schema_d42 % decoded_mocked_body
        except SubstitutionError as e:
            if validate_level == "error":
                raise ValidationException(f"There are some mismatches in {func_name}:\n{str(e)}")
            elif validate_level == "warning":
                print(f"⚠️ There are some mismatches in {func_name} ⚠️:\n{str(e)}")
            elif validate_level == "skip":
                pass

    @staticmethod
    def validate(mocked: _T,
                 prepared_dict_from_spec: Dict[Tuple[str, str], SchemaData],
                 is_strict: bool,
                 validate_level: Literal["error", "warning", "skip"],
                 func_name: str,
                 prefix: str | None) -> None:

        matcher = mocked.handler.matcher.sub_matchers  # type: ignore
        method = matcher[0].sub_matcher.expected
        path = normalize_path(matcher[1].sub_matcher.path, prefix)

        parsed_request = Validator._check_entity_match(prepared_dict_from_spec, http_method=method, path=path)

        if parsed_request:
            if parsed_request.response_schema_d42:
                try:
                    # check for JSON in response of mock
                    decoded_mocked_body = loads(mocked.handler.response.get_body().decode())  # type: ignore
                except JSONDecodeError:
                    raise AssertionError(f"JSON expected in Response body of the {func_name}")

                if is_strict:
                    try:
                        validate_or_fail(parsed_request.response_schema_d42, decoded_mocked_body)
                    except ValidationException as e:
                        raise ValidationException(f"There are some mismatches in {func_name}:{str(e)}")

                    Validator._handle_non_strict_validation_error(parsed_request, decoded_mocked_body, validate_level,
                                                                  func_name)
                else:
                    Validator._handle_non_strict_validation_error(parsed_request, decoded_mocked_body, validate_level,
                                                                  func_name)

            else:
                raise AssertionError(f"API method '{method} {path}' in the spec_link"
                                     f" lacks a response structure for the validation of {func_name}")
        else:
            raise AssertionError(f"API method '{method} {path}' was not found in the spec_link "
                                 f"for the validation of {func_name}")


def _prepare_data(spec_link: str) -> Dict[Tuple[str, str], SchemaData]:
    return load_cache(spec_link)


def validate_spec(*,
                  spec_link: str | None,
                  is_strict: bool = False,
                  validate_level: Literal["error", "warning", "skip"] = "error",
                  prefix: str | None = None) -> Callable[[Callable[..., _T]], Callable[..., _T]]:
    """
       Validates the jj mock function with given specification lint.

       Args:
           spec_link (str | None): The link to the specification. `None` for disable validation.
           is_strict (bool): WIP, only "False" is working now.
           validate_level (Literal["error", "warning", "skip"]): The validation level. Can be 'error', 'warning', or 'skip'. Default is 'error'.
           prefix (str | None): Prefix is used to cut paths prefix in mock function.
       """
    def decorator(func: Callable[..., _T]) -> Callable[..., _T]:
        func_name = func.__name__

        @wraps(func)
        async def async_wrapper(*args: object, **kwargs: object) -> _T:
            if spec_link:
                mocked = await func(*args, **kwargs)
                if isinstance(mocked.handler.response, RelayResponse):
                    print("RelayResponse type is not supported")
                    return mocked
                prepared_dict_from_spec = _prepare_data(spec_link)
                Validator.validate(mocked, prepared_dict_from_spec, is_strict, validate_level, func_name, prefix)
            else:
                mocked = await func(*args, **kwargs)
            return mocked

        @wraps(func)
        def sync_wrapper(*args: object, **kwargs: object) -> _T:
            if spec_link:
                mocked = func(*args, **kwargs)
                if isinstance(mocked.handler.response, RelayResponse):
                    print("RelayResponse type is not supported")
                    return mocked
                prepared_dict_from_spec = _prepare_data(spec_link)
                Validator.validate(mocked, prepared_dict_from_spec, is_strict, validate_level, func_name, prefix)
            else:
                mocked = func(*args, **kwargs)
            return mocked

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    return decorator
