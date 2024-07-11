from datetime import timedelta

from wise.utils.cache import cache_get_key
from wise.utils.redis import get_redis_client


def rate_limit_func(period: int | timedelta):  # period is in seconds
    def decorator(func):
        def wrapper(*args, **kwargs):
            r = get_redis_client()
            cache_key = (
                "_wise:rate_limit:"
                + func.__name__
                + ":"
                + cache_get_key(*args, **kwargs)
            )
            if r.get(cache_key):
                return
            result = func(*args, **kwargs)
            r.set(cache_key, 1, ex=period)
            return result

        return wrapper

    return decorator
