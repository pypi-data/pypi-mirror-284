import functools
import inspect
import logging
import traceback

from beartype import beartype
from beartype.roar import BeartypeCallHintParamViolation
from beartype.typing import Callable, ParamSpec, TypeVar

from misc_python_utils.beartypes import nobeartype
from result import Result, Err

T_co = TypeVar("T_co", covariant=True)  # Success type
E = TypeVar("E")  # Error type
U = TypeVar("U")
F = TypeVar("F")
P = ParamSpec("P")
R = TypeVar("R")
TBE = TypeVar(
    "TBE", bound=Exception
)  # tilo:  original code had "BaseException" here, but thats too liberal! one should not catch SystemExit, KeyboardInterrupt, etc.!


def exceptions_as_err_logged_panic_for_param_violation(
    *exceptions: type[TBE],
) -> Callable[[Callable[P, Result[R, E]]], Callable[P, Result[R, TBE | E]]]:
    """
    exceptions as result but panic for param violations
    """
    return exceptions_as_err_logged(
        *exceptions, panic_exceptions={BeartypeCallHintParamViolation}
    )


def exceptions_as_err_logged(
    *catch_exceptions: type[TBE],
    panic_exceptions: set[type[Exception]]
    | None = None,  # exceptions that are reraised -> panic
) -> Callable[[Callable[P, Result[R, E]]], Callable[P, Result[R, TBE | E]]]:
    """
    based on: https://github.com/rustedpy/result/blob/021d9945f9cad12eb49386691d933c6688ac89a9/src/result/result.py#L439
    :exceptions: exceptions to catch and turn into ``Err(exc)``.
    :panic_exceptions: exceptions to catch and re-raise.
    """
    panic_exceptions = set() if panic_exceptions is None else panic_exceptions
    if panic_exceptions is not None and len(panic_exceptions) > 0:
        _check_for_valid_catch_and_panic_exceptin_combinations(
            set(catch_exceptions), panic_exceptions
        )
    if not catch_exceptions or not all(
        inspect.isclass(exception)
        and issubclass(
            exception, Exception
        )  # tilo: Exception instead of BaseException!
        for exception in catch_exceptions
    ):
        raise TypeError("as_result() requires one or more exception types")

    def decorator(f: Callable[P, Result[R, E]]) -> Callable[P, Result[R, TBE | E]]:
        """
        Decorator to turn a function into one that returns a ``Result``.
        """
        logger = logging.getLogger(
            f.__module__.replace("_", "."),
        )  # "The name is potentially a period-separated hierarchical", see: https://docs.python.org/3.10/library/logging.html

        @functools.wraps(f)
        @nobeartype
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[R, TBE | E]:
            try:
                return beartype(f)(*args, **kwargs)
            except catch_exceptions as exc:
                tb = traceback.format_exc()
                logger.error(tb)  # noqa: TRY400
                if type(exc) in panic_exceptions:
                    raise exc
                return Err(exc)

        return wrapper

    return decorator


def _check_for_valid_catch_and_panic_exceptin_combinations(
    catch_exceptions: set[type[Exception]], panic_exceptions: set[type[Exception]]
):
    panic_exceptions_that_are_not_caught = [
        panic_exc
        for panic_exc in panic_exceptions
        if not any(issubclass(panic_exc, catch_exc) for catch_exc in catch_exceptions)
    ]
    if len(panic_exceptions_that_are_not_caught) > 0:
        raise ValueError(
            f"{panic_exceptions_that_are_not_caught} are not caught by any {catch_exceptions}"
        )


# SomeError = TypeVar(
#     "SomeError"
# )  # tilo: one cannot really know all possible error-types, see "do" notation in result.py
