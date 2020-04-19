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

# Store data for later

array_lengths = [len(random_array_integer_1), 
                 len(random_array_integer_2), 
                 len(random_array_integer_3),
                 len(random_array_integer_4),
                 len(random_array_integer_5),
                 len(random_array_float_1),
                 len(random_array_float_2),
                 len(random_array_float_3),
                 len(random_array_float_4),
                 len(random_array_float_5),
                 len(random_array_string5_1),
                 len(random_array_string5_2),
                 len(random_array_string5_3),
                 len(random_array_string5_4),
                 len(random_array_string5_5),
                 len(random_array_string15_1),
                 len(random_array_string15_2),
                 len(random_array_string15_3),
                 len(random_array_string15_4),
                 len(random_array_string15_5)]

# Define Selection Function to find smallest value

# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Define Sort Function

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

# Generate Times for Selection Sorting Integers

selection_sort_time_integers_1 = timeit.timeit("selectionSort(random_array_integer_1)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_integer_1",
                                               number = 10000)/1000

selection_sort_time_integers_2 = timeit.timeit("selectionSort(random_array_integer_2)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_integer_2",
                                               number = 10000)/1000

selection_sort_time_integers_3 = timeit.timeit("selectionSort(random_array_integer_3)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_integer_3",
                                               number = 10000)/1000

selection_sort_time_integers_4 = timeit.timeit("selectionSort(random_array_integer_4)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_integer_4",
                                               number = 10000)/1000

selection_sort_time_integers_5 = timeit.timeit("selectionSort(random_array_integer_5)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_integer_5",
                                               number = 10000)/1000

# Generate Times for Selection Sorting Floats

selection_sort_time_float_1 = timeit.timeit("selectionSort(random_array_float_1)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_float_1",
                                               number = 10000)/1000

selection_sort_time_float_2 = timeit.timeit("selectionSort(random_array_float_2)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_float_2",
                                               number = 10000)/1000

selection_sort_time_float_3 = timeit.timeit("selectionSort(random_array_float_3)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_float_3",
                                               number = 10000)/1000

selection_sort_time_float_4 = timeit.timeit("selectionSort(random_array_float_4)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_float_4",
                                               number = 10000)/1000

selection_sort_time_float_5 = timeit.timeit("selectionSort(random_array_float_5)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_float_5",
                                               number = 10000)/1000

# Generate Times for Selection Sorting Strings of Length 5

selection_sort_time_string5_1 = timeit.timeit("selectionSort(random_array_string5_1)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string5_1",
                                               number = 10000)/1000

selection_sort_time_string5_2 = timeit.timeit("selectionSort(random_array_string5_2)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string5_2",
                                               number = 10000)/1000

selection_sort_time_string5_3 = timeit.timeit("selectionSort(random_array_string5_3)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string5_3",
                                               number = 10000)/1000

selection_sort_time_string5_4 = timeit.timeit("selectionSort(random_array_string5_4)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string5_4",
                                               number = 10000)/1000

selection_sort_time_string5_5 = timeit.timeit("selectionSort(random_array_string5_5)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string5_5",
                                               number = 10000)/1000

# Generate Times for Selection Sorting Strings of Length 15

selection_sort_time_string15_1 = timeit.timeit("selectionSort(random_array_string15_1)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string15_1",
                                               number = 10000)/1000

selection_sort_time_string15_2 = timeit.timeit("selectionSort(random_array_string15_2)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string15_2",
                                               number = 10000)/1000

selection_sort_time_string15_3 = timeit.timeit("selectionSort(random_array_string15_3)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string15_3",
                                               number = 10000)/1000

selection_sort_time_string15_4 = timeit.timeit("selectionSort(random_array_string15_4)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string15_4",
                                               number = 10000)/1000

selection_sort_time_string15_5 = timeit.timeit("selectionSort(random_array_string15_5)",
                                               setup = "from __main__ import findSmallest, selectionSort, random_array_string15_5",
                                               number = 10000)/1000

# Create dataframe of performance results

d = np.array([[array_lengths[0], 'integer', selection_sort_time_integers_1],
              [array_lengths[1], 'integer', selection_sort_time_integers_2],
              [array_lengths[2], 'integer', selection_sort_time_integers_3],
              [array_lengths[3], 'integer', selection_sort_time_integers_4],
              [array_lengths[4], 'integer', selection_sort_time_integers_5],
              [array_lengths[5], 'float', selection_sort_time_float_1],
              [array_lengths[6], 'float', selection_sort_time_float_2],
              [array_lengths[7], 'float', selection_sort_time_float_3],
              [array_lengths[8], 'float', selection_sort_time_float_4],
              [array_lengths[9], 'float', selection_sort_time_float_5],
              [array_lengths[10], 'string5', selection_sort_time_string5_1],
              [array_lengths[11], 'string5', selection_sort_time_string5_2],
              [array_lengths[12], 'string5', selection_sort_time_string5_3],
              [array_lengths[13], 'string5', selection_sort_time_string5_4],
              [array_lengths[14], 'string5', selection_sort_time_string5_5],
              [array_lengths[15], 'string15', selection_sort_time_string15_1],
              [array_lengths[16], 'string15', selection_sort_time_string15_2],
              [array_lengths[17], 'string15', selection_sort_time_string15_3],
              [array_lengths[18], 'string15', selection_sort_time_string15_4],
              [array_lengths[19], 'string15', selection_sort_time_string15_5]])

cols = ['Length_of_Array', 'Data_Type', 'Selection_Sort_Time']

performance_df = pd.DataFrame(data = d, columns = cols)
performance_df['Selection_Sort_Time'] = performance_df['Selection_Sort_Time'].astype(float)
performance_df['Length_of_Array'] = performance_df['Length_of_Array'].astype(int)

performance_df = performance_df.sort_values(by = 'Selection_Sort_Time')

# Graph Results

plt.rcParams['figure.figsize'] = (15,10)

fig, ax = plt.subplots()

colors = {'integer':'red', 'float':'blue', 'string5':'green', 'string15':'orange'}

ax.scatter(performance_df['Length_of_Array'], 
           performance_df['Selection_Sort_Time'], 
           c = performance_df['Data_Type'].apply(lambda x: colors[x]))

plt.title('Array Size vs Selection Sort Time')
plt.xlabel('Array Size')
plt.ylabel('Search Time (milliseconds)')

plt.show()
