# Packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import random
import timeit

# Set seed
random.seed(123)

# Generate array of random numbers
random_array_1 = np.random.randint(low = 100, high = 500, size= 10)

# Create FOR loop for factorial calculation

def factorial_for_loop_function(x):
    factorial = 1
    if x < 0:
        factorial = None
    elif x == 0:
        factorial = 1
    else:
        for n in range(1, x + 1):
            factorial *= n
    return factorial
    
    # Create array to store times and factorials

for_loop_array = np.empty((0,2), dtype = np.float64)

# Loop through array and store times

for number in random_array_1:
    time = timeit.timeit("factorial_for_loop_function(number)",
                         setup = "from __main__ import factorial_for_loop_function, number, random_array_1",
                         number = 10000)/1000
    for_loop_array = np.append(for_loop_array, np.array([[number, time]]), axis = 0)
    
    # Create factorial calculation with recursion

def factorial_recursion_function(x):
  if x == 1:
    return 1
  else:
    return x * factorial_recursion_function(x-1)
    
    # Create array to store times and factorials

recursion_array = np.empty((0,2), dtype = np.float64)

# Loop through array and store times

for number in random_array_1:
    time = timeit.timeit("factorial_recursion_function(number)",
                         setup = "from __main__ import factorial_recursion_function, number, random_array_1",
                         number = 10000)/1000
    recursion_array = np.append(recursion_array, np.array([[number, time]]), axis = 0)
    
    
    
    
