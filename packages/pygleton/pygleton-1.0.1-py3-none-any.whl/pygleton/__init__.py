"""Singleton implementation."""

from typing import Any, Callable, Generic, Protocol, TypeVar, cast

_I = TypeVar("_I", bound=object)


class _Wrapper(  # pylint: disable=too-few-public-methods
    Generic[_I], Protocol
):
    _instance: None | _I
    _init_called: bool

    def __new__(
        cls: type[_I], *args: Any, **kwargs: Any
    ) -> "_Wrapper[_I]": ...


def singleton(
    recall_init: bool = False,
) -> Callable[[type[_I]], type[_Wrapper[_I]]]:
    """Singleton decorator for class.

    :param recall_init: if truthy, the __init__ method of the original
                        class will be called every time.
    :returns: singleton decorator for a class:
    """

    def _decorator(cls: type[_I]) -> type[_Wrapper[_I]]:

        # pylint: disable=too-few-public-methods
        class Wrapper(cls):  # type: ignore
            """Wrapper class."""

            _instance: None | _I = None
            _init_called = False

            @staticmethod
            def __new__(  # type: ignore
                cls: "type[Wrapper]", *_args: Any, **_kwargs: Any
            ) -> _Wrapper[_I]:
                if Wrapper._instance is None:
                    Wrapper._instance = super().__new__(  # pylint: disable=no-value-for-parameter
                        cls
                    )
                return cast(_Wrapper[_I], Wrapper._instance)

            def __init__(self, *args: Any, **kwargs: Any) -> None:
                if not Wrapper._init_called:
                    Wrapper._init_called = not recall_init
                    super().__init__(*args, **kwargs)

        # pylint: enable=too-few-public-methods

        Wrapper.__name__ = cls.__name__
        Wrapper.__doc__ = cls.__doc__

        return Wrapper

    return _decorator
