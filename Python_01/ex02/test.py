from vector import Vector

print("init\n")

v1 = Vector(5)
print(v1)

v2 = Vector((1, 5))
print(v2)

v3 = Vector([[0.1, 1.0]])
print(v3)

v4 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v4)

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 13.0


print("\ndot()\n")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1)
print(v1.T())

v1 = Vector([[2.0, 2.1, 2.3, 2.4]])
print(v1)
print(v1.T())

print("\nadd\n")
print(Vector([[2.0, 2.1, 2.3, 2.4]]) + Vector([[5.0, 4.9, 4.7, 4.6]]))
print(Vector([[0.0], [1.0], [2.0]]) + Vector([[3.0], [2.0], [1.0]]))
print(Vector([[5.]]) + 4)
print(4 + Vector([[5.]]))
print(Vector([[5.]]) + Vector([[2.]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) + Vector([[0.0], [1.0], [2.0], [3.0]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) + Vector([[2.0, 2.1, 2.3, 2.4, 0.]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) + 5)
# print(5 + Vector([[2.0, 2.1, 2.3, 2.4]]))

print("\nsub\n")
print(Vector([[2.0, 2.1, 2.3, 2.4]]) - Vector([[5.0, 4.9, 4.7, 4.6]]))
print(Vector([[0.0], [1.0], [2.0]]) - Vector([[3.0], [2.0], [1.0]]))
print(Vector([[5.]]) - 4)
print(4 - Vector([[5.]]))
print(Vector([[5.]]) - Vector([[2.]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) - Vector([[0.0], [1.0], [2.0], [3.0]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) - Vector([[2.0, 2.1, 2.3, 2.4, 0.]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) - 5)
# print(5 - Vector([[2.0, 2.1, 2.3, 2.4]]))


print("\nmul\n")
print(Vector([[2.5]]) * Vector([[1.1, 2.2, 3.3, 9.9]]))
print(Vector([[2.5]]) * Vector([[1.1], [2.2], [3.3], [9.9]]))
print(Vector([[1.1, 2.2, 3.3, 9.9]]) * Vector([[2.5]]))
print(Vector([[1.1], [2.2], [3.3], [9.9]]) * Vector([[2.5]]))
print(Vector([[2.]]) * Vector([[21.]]))
print(Vector([[1.1, 2.2, 3.3, 9.9]]) * 2.5)
print(Vector([[1.1], [2.2], [3.3], [9.9]]) * 2.5)
print(2.5 * Vector([[1.1, 2.2, 3.3, 9.9]]))
print(2.5 * Vector([[1.1], [2.2], [3.3], [9.9]]))
# print(Vector([[1., 2.]]) * Vector([[12., 13.]]))


print("\ndiv\n")
# print(Vector([[2.5]]) / Vector([[1.1, 2.2, 3.3, 9.9]]))
# print(Vector([[2.5]]) / Vector([[1.1], [2.2], [3.3], [9.9]]))
print(Vector([[1.1, 2.2, 3.3, 9.9]]) / Vector([[2.5]]))
print(Vector([[1.1], [2.2], [3.3], [9.9]]) / Vector([[2.5]]))
# print(Vector([[2.]]) / Vector([[21.]]))
print(Vector([[1.1, 2.2, 3.3, 9.9]]) / 2.5)
print(Vector([[1.1], [2.2], [3.3], [9.9]]) / 2.5)
# print(2.5 / Vector([[1.1, 2.2, 3.3, 9.9]]))
# print(2.5 / Vector([[1.1], [2.2], [3.3], [9.9]]))
print(5 / Vector([[2.]]))
print(Vector([[5.]]) / 2)

print("\nsubject test\n")

# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)
# Expected output:
# Vector([[0.0], [5.0], [10.0], [15.0]])
print("# Vector([[0.0], [5.0], [10.0], [15.0]])")

# Row vector of shape 1 * n
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
# Expected output
# Vector([[0.0, 5.0, 10.0, 15.0]])
print("# Vector([[0.0, 5.0, 10.0, 15.0]])")
print("########### ", v1)
v2 = v1 / 2.0
print(v2)
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]]) <--------------------- 
print("# Vector([[0.0], [0.5], [1.0], [1.5]])")

# v1 / 0.0
# Expected ouput
# ZeroDivisionError: division by zero.
# print("# ZeroDivisionError: division by zero.")

# 2.0 / v1
# Expected output:
# NotImplementedError: Division of a scalar by a Vector is not defined here.
# print("# NotImplementedError: Division of a scalar by a Vector is not defined here.")

# Column vector of shape (n, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output
# (4,1)
print("# (4,1)")

print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Expected output
# [[0.0], [1.0], [2.0], [3.0]]
print("# [[0.0], [1.0], [2.0], [3.0]]")

# Row vector of shape (1, n)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output
# (1,4)
print("# (1,4)")

print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
# Expected output
# [[0.0, 1.0, 2.0, 3.0]]
print("# [[0.0, 1.0, 2.0, 3.0]]")

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
# Expected output:
# (4,1)
print("# (4,1)")

print(v1.T())
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])
print("# Vector([[0.0, 1.0, 2.0, 3.0]])")

print(v1.T().shape)
# Expected output:
# (1,4)
print("# (1,4)")

# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
# Expected output:
# (1,4)
print("# (1,4)")

print(v2.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print("# Vector([[0.0], [1.0], [2.0], [3.0]])")

print(v2.T().shape)
# Expected output:
# (4,1)
print("# (4,1)")

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
print("# 18.0")

v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output: <--------------------- 
# 13.0
print("# 13.0")

print(v1)
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print("# [[0.0, 1.0, 2.0, 3.0]]")

print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print("# [[0.0, 1.0, 2.0, 3.0]]")
