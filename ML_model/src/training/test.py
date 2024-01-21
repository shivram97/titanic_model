import numpy as np

# Task 1: Create a NumPy array of size 10 filled with zeros.
array_zeros = np.zeros(10)
print("Task 1:", array_zeros)

# Task 2: Create a NumPy array with values ranging from 10 to 49.
array_range = np.arange(10, 50)
print("Task 2:", array_range)

# Task 3: Reshape the above array into a 4x10 matrix.
array_reshaped = array_range.reshape(4, 10)
print("Task 3:")
print(array_reshaped)

# Task 4: Reverse the elements of the above-created 1D array.
array_reversed = np.flip(array_range)
print("Task 4:", array_reversed)

# Task 5: Create a 5x5 identity matrix.
identity_matrix = np.eye(5)
print("Task 5:")
print(identity_matrix)

# Task 6: Extract the integer part of a random array using 5 different methods.
random_array = np.random.rand(5) * 10  # Generating random array
print("Task 6:")
print(random_array)

# Different methods to extract integer part
print("Method 1:", random_array.astype(int))
print("Method 2:", np.trunc(random_array))
print("Method 3:", np.floor(random_array))
print("Method 4:", np.ceil(random_array) - 1)
print("Method 5:", np.round(random_array))

# Task 7: Create a 10x10 array with random values and find the minimum and maximum values. Add a border around the existing array.
random_10x10_array = np.random.rand(10, 10)
print("Task 7:")
print("Original Array:")
print(random_10x10_array)

min_value = np.min(random_10x10_array)
max_value = np.max(random_10x10_array)

# Adding a border filled with 0's
bordered_array = np.pad(random_10x10_array, pad_width=1, mode='constant', constant_values=0)

print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Array with Border:")
print(bordered_array)

# Task 8: Create a random 2D array and replace all elements that are greater than a specified value with 0.
random_2d_array = np.random.rand(3, 4) * 10
print("Task 8:")
print("Original 2D Array:")
print(random_2d_array)

specified_value = 5
random_2d_array[random_2d_array > specified_value] = 0

print("Array after replacement:")
print(random_2d_array)

# Task 9: Multiply a 5x3 matrix by a 3x2 matrix containing random integer elements.
matrix_5x3 = np.random.randint(1, 10, size=(5, 3))
matrix_3x2 = np.random.randint(1, 10, size=(3, 2))
result_matrix = np.dot(matrix_5x3, matrix_3x2)
print("Task 9:")
print("Matrix 5x3:")
print(matrix_5x3)
print("Matrix 3x2:")
print(matrix_3x2)
print("Result Matrix:")
print(result_matrix)

# Task 10: Create a random array and filter the numbers which are divisible by a specific number (e.g., 3).
random_array_for_divisibility = np.random.randint(1, 100, size=10)
divisor = 3
filtered_array = random_array_for_divisibility[random_array_for_divisibility % divisor == 0]
print("Task 10:")
print("Random Array:")
print(random_array_for_divisibility)
print("Filtered Array (divisible by", divisor, "):")
print(filtered_array)

# Task 11: Find the mean, median, standard deviation of a random array.
random_array_for_statistics = np.random.rand(10)
mean_value = np.mean(random_array_for_statistics)
median_value = np.median(random_array_for_statistics)
std_deviation_value = np.std(random_array_for_statistics)
print("Task 11:")
print("Random Array:")
print(random_array_for_statistics)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation_value)

# Task 12: Normalize a 5x5 random matrix (subtract the mean and divide by the standard deviation).
random_matrix_for_normalization = np.random.rand(5, 5) * 10
normalized_matrix = (random_matrix_for_normalization - np.mean(random_matrix_for_normalization)) / np.std(random_matrix_for_normalization)
print("Task 12:")
print("Original Matrix:")
print(random_matrix_for_normalization)
print("Normalized Matrix:")
print(normalized_matrix)

# Task 13: Create a 5x5 matrix with values 1,2,3,4 just below the diagonal.
diagonal_matrix = np.diag(np.arange(1, 5), k=-1)
print("Task 13:")
print(diagonal_matrix)

# Task 14: Create a random array and sort it along the first axis and then the last axis.
random_array_for_sorting = np.random.randint(1, 100, size=(4, 3))
print("Task 14:")
print("Original Array:")
print(random_array_for_sorting)

sorted_array_axis0 = np.sort
