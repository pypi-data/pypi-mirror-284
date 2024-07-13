Credit to https://www.kaggle.com/code/stassl/displaying-inline-images-in-pandas-dataframe.

Usage example:
```python
from datasets import load_dataset
# Load Fashion MNIST dataset
rows = load_dataset("zalando-datasets/fashion_mnist", split="test")
rows.set_format(type="pandas") # rows is a datasets.Dataset object from Hugging Face
df = rows[:]

from draxutils import show_pd
show_pd(df)

# if there is a column with multiple images, you can specify the column name
# show_pd(df, imglist_key='mycol')
```

```python
# Timer Usage Example

from simple_timer import timer, time_this, timed
import time

# Example 1: Using the timer as a context manager
print("Example 1: Context Manager")
with timer:
    time.sleep(1)  # Simulate some work
print(timer)  # Output the elapsed time

# Example 2: Using the time_this generator
print("\nExample 2: time_this Generator")
for _ in time_this():
    time.sleep(0.5)  # Simulate some work
print(timer)  # Output the elapsed time

# Example 3: Using the timer as a decorator
print("\nExample 3: Decorator")
@timed
def some_function():
    time.sleep(0.75)  # Simulate some work

some_function()
print(f"Function execution time: {some_function.elapsed:.6f} seconds")

# Example 4: Manual usage
print("\nExample 4: Manual Usage")
timer.start_time = time.time()  # Start the timer manually
time.sleep(1.25)  # Simulate some work
timer.end_time = time.time()  # Stop the timer manually
print(f"Manual timing: {timer.elapsed:.6f} seconds")

# Example 5: Nested timers
print("\nExample 5: Nested Timers")
with timer:
    print("Outer timer started")
    time.sleep(0.5)
    with Timer() as inner_timer:
        print("Inner timer started")
        time.sleep(0.75)
    print(f"Inner timer: {inner_timer}")
print(f"Outer timer: {timer}")
```