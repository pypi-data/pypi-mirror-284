from datetime import datetime, timedelta

class RateLimiter:
    _instance = None
    _params = {}

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

            cls._instance.request_counts = {}
            cls._instance.request_timestamps = {}
            cls._instance.rate_limit_hit_count = {}
            cls._instance.wait_start_times = {}
        return cls._instance

    def is_rate_limited(self, ip):
        now = datetime.utcnow()

        self.request_counts[ip] = self.request_counts.get(ip, 0) + 1
        if not ip in self.wait_start_times:
            self.wait_start_times[ip] = now
        else:
            self.wait_start_times[ip] = self.wait_start_times.get(ip, now)

        self.rate_limit_hit_count[ip] = self.rate_limit_hit_count.get(ip, 0)
        if ip not in self.request_timestamps:
            self.request_timestamps[ip] = []

        self.request_timestamps[ip].append(now)

        self.clear_old_entries(now)

        print(self.request_counts[ip])

        if self.request_counts[ip] >= self.limit:
            if ip in self.rate_limit_hit_count:
                self.rate_limit_hit_count[ip] += 1
            else:
                self.rate_limit_hit_count[ip] = 1
            if self.has_wait_time_passed(ip):
                return False
            return True
        else:
            return False

    def clear_old_entries(self, current_time):
        MAX_ENTRY_AGE = timedelta(minutes=4)
        keys_to_remove = []

        for ip, timestamps in self.request_timestamps.items():
            timestamps.sort(reverse=True)

            for i, timestamp in enumerate(timestamps):
                age_of_entry = current_time - timestamp
                if age_of_entry > MAX_ENTRY_AGE:
                    keys_to_remove.append((ip, timestamp))
                    break

        for ip, timestamp in keys_to_remove:
            try:
                timestamps.remove(timestamp)
                if not timestamps:
                    del self.request_counts[ip]
                    del self.rate_limit_hit_count[ip]
                    del self.wait_start_times[ip]
                    if not self.request_timestamps[ip]:
                        del self.request_timestamps[ip]
            except ValueError:
                pass

    def has_wait_time_passed(self, ip):
        now = datetime.utcnow()

        if ip in self.wait_start_times:
            wait_start = self.wait_start_times[ip]
        else:
            wait_start = now

        if wait_start is None:
            self.wait_start_times[ip] = now
            return True

        wait_duration = now - wait_start
        total_wait_duration = min(self.rate_limit_hit_count[ip], self.max_wait_time)

        if wait_duration.total_seconds() < total_wait_duration:
            return False

        self.wait_start_times[ip] = None
        self.request_counts[ip] = 0
        self.rate_limit_hit_count[ip] = 0
        return True

    def get_remaining_wait_time(self, ip):
        now = datetime.utcnow()
        if ip in self.wait_start_times:
            wait_start = self.wait_start_times[ip]
        else:
            wait_start = now

        if wait_start is None:
            return 0

        hit_count = self.rate_limit_hit_count[ip]
        total_wait_duration = min(hit_count, self.max_wait_time)

        effective_wait_end = wait_start + timedelta(seconds=total_wait_duration)
        remaining_wait = max(0, (effective_wait_end - now).total_seconds())

        return remaining_wait
