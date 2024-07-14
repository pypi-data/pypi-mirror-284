from functools import wraps
from flask import jsonify, request
from .rate_limiter import RateLimiter
import math

def rate_limited(limit, period, max_wait_time):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(*args, **kwargs):
            limiter = RateLimiter.get_instance()
            limiter.limit = 4
            limiter.period = 4
            limiter.max_wait_time = 60

            ip = request.headers['X-Real-Ip']

            if limiter and limiter.is_rate_limited(ip):
                time_left = limiter.get_remaining_wait_time(ip)
                return jsonify({'error': 'Rate limit exceeded', 'message': f'Please wait {math.ceil(time_left)} seconds before trying again'}), 429

            return view_func(*args, **kwargs)
        return _wrapped_view
    return decorator
