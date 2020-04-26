# Packages
import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import timeit

# Set seed
random.seed(123)

# Generate array of random numbers

random_array_1 = [random.randint(100, 500) for x in range(10)]

# Create FOR loop for factorial calculation

def factorial_for_loop_function(x):
    factorial = 1
    if x <= 0:
        factorial = None
    elif x == 0:
        factorial = 1
    else:
        for n in range(1, (x + 1)):
            factorial *= n
    return factorial
    
# Create array to store times and factorials

for_loop_array = np.empty((0,2), dtype = np.float64)

# Create array to store times and factorials

for_loop_array = np.empty((0,2))

# Loop through array and store times

for number in random_array_1:
    time = timeit.timeit("factorial_for_loop_function(number)",
                         setup = "from __main__ import factorial_for_loop_function, number, random_array_1",
                         number = 10000)/1000
    for_loop_array = np.append(for_loop_array, np.array([[number, time]]), axis = 0)
    
# Create factorial calculation with recursion

def factorial_recursion_function(x):
    if x <= 0:
        return None
    elif x == 1:
        return 1
    else:
        return x * factorial_recursion_function(x - 1)
    
# Create array to store times and factorials

recursion_array = np.empty((0,2))

# Loop through array and store times

for number in random_array_1:
    time = timeit.timeit("factorial_recursion_function(number)",
                         setup = "from __main__ import factorial_recursion_function, number, random_array_1",
                         number = 10000)/1000
    recursion_array = np.append(recursion_array, np.array([[number, time]]), axis = 0)
    
# Create dataframe for results

data = {'Number': random_array_1,         
        'Recursion Time': recursion_array[...,1],
        'For Loop Time': for_loop_array[...,1],
        'Difference': recursion_array[...,1] - for_loop_array[...,1]}

results_df = pd.DataFrame(data).sort_values('Number')

# Plot Results

plt.plot('Number', 'Recursion Time', data = results_df,
        marker='', color='red', linewidth=2, label = 'Recursion')
plt.plot('Number', 'For Loop Time', data = results_df,
        marker='', color='blue', linewidth=2, label = 'Loop')

plt.title('Number vs Factorial Function Time')
plt.xlabel('Number')
plt.ylabel('Function Time (milliseconds)')

plt.legend()

# Create factorial calculation with larger recursion limit

def factorial_recursion_function_2(x):
    if x <= 0:
        return None
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return x * (x - 1) * factorial_recursion_function_2(x - 2)
    
# Recursion function for looking at filed in directory 
    
def list_files(filepath):
    if os.path.isfile(filepath):
        print(filepath)
    else:
        for item in os.listdir(filepath):
            list_files(filepath + '/' + item)
    
    
    
    
