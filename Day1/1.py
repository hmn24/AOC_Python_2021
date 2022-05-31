import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# Read files
with open("1.txt") as f:
    lines = f.readlines()

# Use numpy
numbers = np.array([int(i) for i in lines])

# Part 1
p1 = np.sum((numbers[1:] - numbers[:-1]) > 0)
print(f"Part 1 answer is {p1}")

# Part 2
sliding_window_numbers = np.array(
    [np.sum(i) for i in sliding_window_view(numbers, window_shape=3)]
)
p2 = np.sum((sliding_window_numbers[1:] - sliding_window_numbers[:-1]) > 0)
print(f"Part 2 answer is {p2}")

# import code; code.interact(local=dict(globals(), **locals()))
