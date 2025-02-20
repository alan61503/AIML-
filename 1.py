import numpy as np

# 1. Import NumPy

# 2. Create a 1-D array
np1 = np.array([5,7,3,5,8,9,4,5,6,1])
print(np1)

# 3. Create a 2-D array
np2 = np.array([[5,7,3,5,8], [9,4,5,6,1]])
print(np2)

# 4. Print entire arrays
print(np1)
print(np2)

# 5. Print the 6th element of 1D array
print(np1[5])

# 6. Print the 6th element using negative indexing
print(np1[-5])

# 7. Print all elements from the 4th element onward
print(np1[3:])
print(np1[-7:])

# 8. Print numbers at odd positions
print(np1[::2])

# 9. Print elements at positions 0, 3, 6, 9
print(np1[[0,3,6,9]])

# 10. Print only `7` in the 2D array
print(np2[0,1])

# 11. Print selected elements from 2D array
print(np2[:, 1:3])

# 12. Print `[7,3]` from 2D array
print(np2[0,1:3])

# 13. Use mathematical functions
print(np.sqrt(np1))
print(np.min(np1))
print(np.max(np1))
print(np.abs(np1))
print(np.exp(np1))
print(np.sign(np1))
print(np.sin(np1), np.cos(np1), np.log(np1+1))

# 14. Find shape of arrays
print(np1.shape)
print(np2.shape)

# 15. Perform reshaping
reshaped = np1.reshape(2, 5)
print(reshaped)

# 16. Create string arrays
str1 = np.array(["apple", "banana", "cherry"])
str2 = np.array([["red", "green"], ["yellow", "blue"]])
print(str1, str2)

# 17. Sort an array
print(np.sort(np1))

# 18. Print all elements using a loop
for i in np1:
    print(i, end=" ")

# 19. Create a 3×3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# 20. Convert list to NumPy array and multiply by 3
arr = np.array([5, 10, 15, 20]) * 3
print(arr)

# 21. Create arrays of zeros and ones
zeros = np.zeros((4,2))
ones = np.ones((3,3))
print(zeros, ones)

# 22. Extract second row from 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1])

# 23. Reverse an array
arr = np.array([10, 20, 30, 40, 50])
print(arr[::-1])

# 24. Extract elements greater than 15 from 5×5 matrix
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[matrix > 15])

# 25. Reshape a 1D array of size 12 into 3×4
arr = np.arange(12).reshape(3, 4)
print(arr)

# 26. Concatenate arrays horizontally and vertically
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack((a, b)))
print(np.vstack((a, b)))

# 27. Split an array into 3 parts
arr = np.array([10, 20, 30, 40, 50])
print(np.array_split(arr, 3))

# 28. Compute element-wise product
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
print(a * b)

# 29. Sum elements along rows and columns
matrix = np.random.randint(1, 10, (3, 3))
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))

# 30. Compute dot product of two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))

# 31. Replace even numbers with -1
arr = np.arange(1, 21)
arr[arr % 2 == 0] = -1
print(arr)

# 32. Create a boolean mask
arr = np.array([3, 6, 9, 12, 15])
mask = arr > 10
print(arr[mask])

# 33. Extract elements from a 2D array
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr[1])
print(arr[:, 1])

# 34. Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.matmul(A, B))

# 35. Generate a 4×4 random matrix and compute stats
arr = np.random.randint(1, 100, (4, 4))
print(np.max(arr, axis=1))
print(np.sum(arr))
print(np.mean(arr))

# 36. Replace values and count elements
arr = np.array([[12, 18, 5], [23, 9, 15], [8, 6, 30]])
arr[arr > 15] = 0
print(arr)
print(np.sum(arr < 10))
