import sys
import time
import logging
import functools
import asyncio
from typing import Callable, TypeVar, Type, Optional, Coroutine, Any, Awaitable

if sys.version_info >= (3, 10):  # pragma: no cover
    from typing import ParamSpec
else:  # pragma: no cover
    from typing_extensions import ParamSpec


P = ParamSpec('P')
R = TypeVar('R')
OF = Callable[P, R]
DF = Callable[P, Optional[R]]
# Coroutine[Any, Any, str]
AOF = Callable[P, Coroutine[Any, Any, R]]
ADF = Callable[P, Coroutine[Any, Any, Optional[R]]]


def retry(*exceptions: Type[Exception],
          retry: bool = True,
          attempts: int = 3,
          wait: float = 1,
          reraise: bool = True,
          logger: Callable = logging.debug
          ) -> Callable[[OF], DF]:
    """if retry is True , retry when the decorated function throws the *SPECIFIED* exceptions.
if retry is False , retry when the decorated function throws the *UNSPECIFIED* exceptions.
    """
    for exc in exceptions:
        assert issubclass(exc, Exception), \
            f"{exc} is not a Exception type."  # type:ignore

    def decorator(func: OF) -> DF:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            except_occurs: None | Exception = None
            err_type: None | type[Exception] = None
            for _ in range(attempts):
                except_occurs = None
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    except_occurs = err
                    err_type = type(except_occurs)
                    assert err_type is not None
                    if retry == True and err_type in exceptions:
                        logger(f"{func.__name__} raise {err_type.__name__} "
                               f"in specified list, will try again.")
                    elif retry == False and err_type not in exceptions:
                        logger(f"{func.__name__} raise {err_type.__name__} "
                               f"not in specified list, will try again.")
                    else:
                        logger(f"{func.__name__} raise {err_type.__name__}, "
                               f"will not retry.")
                        break
                time.sleep(wait)
            assert except_occurs is not None
            assert err_type is not None
            if reraise == True:
                logger(f"{func.__name__} will reraise {err_type.__name__}.")
                raise except_occurs
            else:
                logger(f"{func.__name__} will not reraise {err_type.__name__}.")
            return None
        return wrapper
    return decorator


def async_retry(*exceptions: Type[Exception],
                retry: bool = True,
                attempts: int = 3,
                wait: float = 1,
                reraise: bool = True,
                logger: Callable = logging.debug
                ) -> Callable[[AOF], ADF]:
    """if retry is True , retry when the decorated function throws the *SPECIFIED* exceptions.
if retry is False , retry when the decorated function throws the *UNSPECIFIED* exceptions.
    """
    for exc in exceptions:
        assert issubclass(exc, Exception), \
            f"{exc} is not a Exception type."  # type:ignore

    def decorator(func: AOF) -> ADF:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs):
            except_occurs: None | Exception = None
            err_type: None | type[Exception] = None
            for _ in range(attempts):
                except_occurs = None
                try:
                    return await func(*args, **kwargs)
                except Exception as err:
                    except_occurs = err
                    err_type = type(except_occurs)
                    assert err_type is not None
                    if retry == True and err_type in exceptions:
                        logger(f"{func.__name__} raise {err_type.__name__} "
                               f"in specified list, will try again.")
                    elif retry == False and err_type not in exceptions:
                        logger(f"{func.__name__} raise {err_type.__name__} "
                               f"not in specified list, will try again.")
                    else:
                        logger(f"{func.__name__} raise {err_type.__name__}, "
                               f"will not retry.")
                        break
                await asyncio.sleep(wait)
            assert except_occurs is not None
            assert err_type is not None
            if reraise == True:
                logger(f"{func.__name__} will reraise {err_type.__name__}.")
                raise except_occurs
            else:
                logger(f"{func.__name__} will not reraise {err_type.__name__}.")
            return None
        return wrapper
    return decorator
