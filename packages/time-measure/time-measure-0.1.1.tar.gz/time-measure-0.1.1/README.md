# Time measure: an easy way to measure elapsed time in python

## Features

- Decorator for measuring function execution time
- Context manager for measuring code block execution time
- Function wrapper for measuring function calls
- Standalone function for one-off time measurements

## Installation

```bash
pip install time-measure
```

## Usage

### Standalone Function

Use measure_time() for one-off time measurements:

```python
from time_measure import measure_time

def my_function(n):
    return sum(range(n))

measure_time(my_function, 10**7)
```

### Decorator

Use the @time_measure_decorator() to measure function execution time:

```python
from time_measure import time_measure_decorator

@time_measure_decorator()
def my_function(n):
    return sum(range(n))

my_function(10**7)
my_function(10**8)
my_function.print_stats()
```

### Context manager

Function-based

Use time_measure_context() to measure execution time of a code block:

```python
from time_measure import time_measure_context

with time_measure_context("my_function (time_measure_context)"):
    # Your code here
    sum(range(10**7))
```

Class-based

Use TimeMeasureContextManager for more control and multiple measurements:

```python
from time_measure import TimeMeasureContextManager

time_measure_context = TimeMeasureContextManager("my_function (TimeMeasureContextManager)")

with time_measure_context():
    sum(range(10**7))

with time_measure_context():
    sum(range(10**8))
    sum(range(10**7))

time_measure_context.print_stats()
```

### Function wrapper

Function-based

Wrap a function to measure its execution time:

```python
from time_measure import time_measure_decorator

def my_function(n):
    return sum(range(n))

wrapped_function = time_measure_decorator(my_function)
wrapped_function(10**7)
wrapped_function(10**8)
wrapped_function.print_stats()
```

Class-based

Use TimeMeasureWrapper for more control:

```python
from time_measure import TimeMeasureWrapper

def my_function(n):
    return sum(range(n))

time_measure_wrapper = TimeMeasureWrapper()
wrapped_function = time_measure_wrapper(my_function)
wrapped_function(10**7)
wrapped_function(10**8)
time_measure_wrapper.print_stats(my_function.__name__)
```

## Output

The tool provides detailed timing information, including:

- Execution time for each call
- Average execution time
- Total execution time
- Number of calls

Example output at runtime:
```
[INFO] my_function (call 1): 0.088180 seconds (avg: 0.088180 seconds, total: 0.088180 seconds)
[INFO] my_function (call 2): 0.826875 seconds (avg: 0.457527 seconds, total: 0.915055 seconds)
```

Example output from a print_stats() call:
```
[INFO] my_function stats:
  Calls: 2
  Total time: 0.915055 seconds
  Average time: 0.457527 seconds
```

## Contributing

If you encounter any issues or have suggestions for improvement, please open an issue in the repository or create a Pull Request.

## License

This project is licensed under the MIT License.