import time
from functools import wraps
from contextlib import contextmanager

class TimeMeasureStats:
    def __init__(self, name):
        self.name = name
        self.call_count = 0
        self.total_time = 0

    def update(self, duration):
        self.call_count += 1
        self.total_time += duration

    def print_stats(self):
        if self.call_count == 0:
            print(f"[INFO] {self.name} has not been called yet.")
        else:
            avg_time = self.total_time / self.call_count
            print(f'[INFO] {self.name} stats:'
                  f'\n  Calls: {self.call_count}'
                  f'\n  Total time: {self.total_time:.6f} seconds'
                  f'\n  Average time: {avg_time:.6f} seconds')

class TimeMeasureWrapper:
    def __init__(self):
        self.stats = {}

    def __call__(self, func):
        if func.__name__ not in self.stats:
            self.stats[func.__name__] = TimeMeasureStats(func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.monotonic()
            result = func(*args, **kwargs)
            end_time = time.monotonic()
            duration = end_time - start_time

            stats = self.stats[func.__name__]
            stats.update(duration)

            print(f'[INFO] {func.__name__} (call {stats.call_count}): {duration:.6f} seconds '
                  f'(avg: {stats.total_time / stats.call_count:.6f} seconds, '
                  f'total: {stats.total_time:.6f} seconds)')

            return result

        def print_stats():
            self.print_stats(func.__name__)

        wrapper.print_stats = print_stats
        return wrapper

    def print_stats(self, func_name):
        if func_name not in self.stats:
            print(f"[INFO] {func_name} has not been called yet.")
        else:
            self.stats[func_name].print_stats()

class TimeMeasureContextManager:
    def __init__(self, name: str = "TimeMeasureContextManager"):
        self.stats = TimeMeasureStats(name)
        self.name = name

    def __call__(self):
        @contextmanager
        def context_manager():
            start_time = time.monotonic()
            yield
            end_time = time.monotonic()
            duration = end_time - start_time
            self.stats.update(duration)
            print(f'[INFO] {self.name} (call {self.stats.call_count}): {duration:.6f} seconds '
                  f'(avg: {self.stats.total_time / self.stats.call_count:.6f} seconds, '
                  f'total: {self.stats.total_time:.6f} seconds)')

        return context_manager()

    def print_stats(self):
        self.stats.print_stats()

def time_measure_decorator(func=None):
    wrapper = TimeMeasureWrapper()
    if func is None:
        return wrapper
    else:
        return wrapper(func)

@contextmanager
def time_measure_context(name: str = "time_measure_context"):
    start_time = time.monotonic()
    yield
    end_time = time.monotonic()
    duration = end_time - start_time
    print(f'[INFO] {name}: {duration:.6f} seconds')

def measure_time(func, *args, **kwargs):
    start_time = time.monotonic()
    result = func(*args, **kwargs)
    end_time = time.monotonic()
    duration = end_time - start_time
    print(f'[INFO] {func.__name__}: {duration:.6f} seconds')
    return result