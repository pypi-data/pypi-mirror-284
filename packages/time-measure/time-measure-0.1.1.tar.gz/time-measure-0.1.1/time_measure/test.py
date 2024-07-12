from time_measure import time_measure_decorator, time_measure_context, TimeMeasureContextManager, TimeMeasureWrapper, measure_time

def test_function(n):
    return sum(range(n))

def test_function_2(n):
    return sum(range(n))

# Test decorator
@time_measure_decorator()
def decorated_function(n):
    return test_function(n)

# Test context manager (function)
def test_context_manager_function():
    with time_measure_context("test_context_manager_function"):
        test_function(10**7)

# Test context manager (class)
def test_context_manager_class():
    time_measure_context = TimeMeasureContextManager("test_context_manager_class")
    with time_measure_context():
        test_function(10**7)
    with time_measure_context():
        test_function(10**7)
    time_measure_context.print_stats()

# Test function wrapper (function)
def test_function_wrapper_function():
    wrapped_function = time_measure_decorator(test_function)
    wrapped_function(10**7)
    wrapped_function(10**7)
    wrapped_function.print_stats()

# Test function wrapper (class)
def test_function_wrapper_class():
    time_measure_wrapper = TimeMeasureWrapper()
    wrapped_function = time_measure_wrapper(test_function)
    wrapped_function(10**7)
    wrapped_function(10**8)
    time_measure_wrapper.print_stats(test_function.__name__)

def test_function_measurement():
    measure_time(test_function, 10**7)

def run_tests():
    print("Testing decorator:")
    decorated_function(10**7)
    decorated_function(10**8)
    decorated_function.print_stats()
    print("\nTesting context manager (function):")
    test_context_manager_function()
    print("\nTesting context manager (class):")
    test_context_manager_class()
    print("\nTesting function wrapper (function):")
    test_function_wrapper_function()
    print("\nTesting function wrapper (class):")
    test_function_wrapper_class()

if __name__ == "__main__":
    run_tests()