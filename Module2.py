# Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import string
import timeit

# Set seed
random.seed(123)

# Generate arrays of random integers

random_array_integer_1 = list(np.random.randint(low = 1, high = 25000, size= 5000))
random_array_integer_2 = list(np.random.randint(low = 1, high = 25000, size= 10000))
random_array_integer_3 = list(np.random.randint(low = 1, high = 25000, size= 15000))
random_array_integer_4 = list(np.random.randint(low = 1, high = 25000, size= 20000))
random_array_integer_5 = list(np.random.randint(low = 1, high = 25000, size= 25000))

# Generate arrays of random floats

random_array_float_1 = list(np.random.uniform(low = 1, high = 25000, size= 5000))
random_array_float_2 = list(np.random.uniform(low = 1, high = 25000, size= 10000))
random_array_float_3 = list(np.random.uniform(low = 1, high = 25000, size= 15000))
random_array_float_4 = list(np.random.uniform(low = 1, high = 25000, size= 20000))
random_array_float_5 = list(np.random.uniform(low = 1, high = 25000, size= 25000))
              
# Generate arrays of random strings of length 5

random_array_string5_1 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(5000)]
random_array_string5_2 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(10000)]
random_array_string5_3 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(15000)]
random_array_string5_4 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(20000)]
random_array_string5_5 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(25000)]

# Generate arrays of random strings of length 15

random_array_string15_1 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(5000)]
random_array_string15_2 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(10000)]
random_array_string15_3 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(15000)]
random_array_string15_4 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(20000)]
random_array_string15_5 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(25000)]

















