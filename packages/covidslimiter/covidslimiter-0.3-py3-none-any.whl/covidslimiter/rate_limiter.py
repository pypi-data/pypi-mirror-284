from datetime import datetime, timedelta
from expiringdict import ExpiringDict

class RateLimiter:
    _instance = None
    _params = {}
    MAX_ENTRY_AGE = timedelta(minutes=4)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RateLimiter, cls).__new__(cls)
            cls._params = {'limit': kwargs.get('limit'), 'period': kwargs.get('period'), 'max_wait_time': kwargs.get('max_wait_time')}
        return cls._instance

    @classmethod
    def get_instance(cls, limit=None, period=None, max_wait_time=None):
        if not cls._instance:
            cls._instance = cls()
            for attr_name, param_value in cls._params.items():
                setattr(cls._instance, attr_name, param_value)

            cls._instance.request_counts = ExpiringDict(max_len=10000, max_age_seconds=int(MAX_ENTRY_AGE.total_seconds()))
            cls._instance.first_request_times = ExpiringDict(max_len=10000, max_age_seconds=int(MAX_ENTRY_AGE.total_seconds()))
            cls._instance.rate_limit_hit_count = ExpiringDict(max_len=10000, max_age_seconds=int(MAX_ENTRY_AGE.total_seconds()))
            cls._instance.wait_start_times = ExpiringDict(max_len=10000, max_age_seconds=int(MAX_ENTRY_AGE.total_seconds()))
            cls._instance.wait_time_passed = ExpiringDict(max_len=10000, max_age_seconds=int(MAX_ENTRY_AGE.total_seconds()))
        return cls._instance

    def is_rate_limited(self, ip):
        now = datetime.utcnow()

        self.clear_old_entries(now)

        self.request_counts[ip] = self.request_counts.get(ip, 0)
        self.first_request_times[ip] = self.first_request_times.get(ip, None)
        self.rate_limit_hit_count[ip] = self.rate_limit_hit_count.get(ip, 0)
        self.wait_start_times[ip] = self.wait_start_times.get(ip, None)
        self.wait_time_passed[ip] = self.wait_time_passed.get(ip, False)

        self.request_counts[ip] += 1

        if self.first_request_times[ip] is None or self.first_request_times[ip] <= now - self.period:
            if self.request_counts[ip] >= self.limit:
                self.rate_limit_hit_count[ip] += 1
                if self.wait_start_times[ip] is None:
                    self.wait_start_times[ip] = now
                    self.wait_time_passed[ip] = False
                if self.has_wait_time_passed(ip):
                    return False
                return True
            else:
                return False
        elif self.get_remaining_wait_time(ip) <= 0:
            self.first_request_times[ip] = now
            self.request_counts[ip] = 1
            return False
        else:
            return True

    def clear_old_entries(self, current_time, size_thresholds: int = 50):
        keys_to_remove = []
        for ip, request_count in self.request_counts.items():
            if current_time - self.first_request_times[ip] > self.MAX_ENTRY_AGE:
                keys_to_remove.append(ip)

        for ip in keys_to_remove:
            del self.request_counts[ip]
            del self.first_request_times[ip]
            del self.rate_limit_hit_count[ip]
            del self.wait_start_times[ip]
            del self.wait_time_passed[ip]

        for key_dict, size_threshold in zip([self.request_counts, self.first_request_times, self.rate_limit_hit_count, self.wait_start_times, self.wait_time_passed], size_thresholds):
            while len(key_dict) > size_threshold:
                oldest_key = min(key_dict.keys(), key=lambda k: key_dict[k])
                del key_dict[oldest_key]

    def has_wait_time_passed(self, ip):
        now = datetime.utcnow()
        wait_start = self.wait_start_times[ip]

        if wait_start is None:
            return True

        wait_duration = now - wait_start
        total_wait_duration = min(self.rate_limit_hit_count[ip], self.max_wait_time)

        if wait_duration.total_seconds() < total_wait_duration:
            return False

        self.wait_time_passed[ip] = True
        self.wait_start_times[ip] = None
        self.request_counts[ip] = 0
        self.rate_limit_hit_count[ip] = 0
        return True

    def get_remaining_wait_time(self, ip):
        now = datetime.utcnow()
        wait_start = self.wait_start_times[ip]

        if wait_start is None:
            return 0

        hit_count = self.rate_limit_hit_count[ip]
        total_wait_duration = min(hit_count, self.max_wait_time)

        effective_wait_end = wait_start + timedelta(seconds=total_wait_duration)
        remaining_wait = max(0, (effective_wait_end - now).total_seconds())

        return remaining_wait
