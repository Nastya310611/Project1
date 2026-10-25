from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, TypeVar, Any

P = ParamSpec('P')
T = TypeVar('T')

def log(filename: str | None =None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            message = ""
            call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                message = f"[{call_time}] {func.__name__} ok. Result: {result}"
            except Exception as error:
                message = f"[{call_time}] {func.__name__} error: {str(error)}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
            return result

        return wrapper

    return decorator
