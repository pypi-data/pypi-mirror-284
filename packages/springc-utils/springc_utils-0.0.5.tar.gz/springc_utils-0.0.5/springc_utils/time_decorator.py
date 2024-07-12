import time
from functools import wraps

def timing_decorator(logging):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            message = f"Function '{func.__name__}' executed in {execution_time:.4f} seconds"
            logging.info(message)
            return result
        return wrapper
    return decorator