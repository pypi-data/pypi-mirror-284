import inspect
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar, cast

P = ParamSpec("P")
R = TypeVar("R")


class MemoizedFunction(Callable[P, R]):
    def __init__(self, func: Callable[P, R]):
        self.func = func
        self.name = func.__name__
        self.signature = inspect.signature(func)
        self.arg_info = self._get_arg_info()
        self.return_type = self._get_return_type()
        self.docstring = func.__doc__

    def _get_arg_info(self) -> dict:
        return {
            name: {
                "annotation": param.annotation,
                "default": param.default if param.default is not param.empty else None,
                "kind": param.kind,
            }
            for name, param in self.signature.parameters.items()
        }

    def _get_return_type(self) -> Any:
        return (
            self.signature.return_annotation if self.signature.return_annotation is not inspect.Signature.empty else Any
        )

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.func(*args, **kwargs)

    def get_full_contract(self) -> dict:
        return {
            "name": self.name,
            "arguments": self.arg_info,
            "return_type": self.return_type,
            "docstring": self.docstring,
        }


def function():
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return cast(R, MemoizedFunction(func)(*args, **kwargs))

        return wrapper

    return decorator
