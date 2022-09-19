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
print()
print(Vector([[0.0], [1.0], [2.0]]) + Vector([[3.0], [2.0], [1.0]]))
print()
print(Vector([[5.]]) + 4)
print()
print(4 + Vector([[5.]]))
print()

# print(Vector([[2.0, 2.1, 2.3, 2.4]]) + Vector([[0.0], [1.0], [2.0], [3.0]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) + Vector([[2.0, 2.1, 2.3, 2.4, 0.]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) + 5)
# print(5 + Vector([[2.0, 2.1, 2.3, 2.4]]))

print("\nsub\n")
print(Vector([[2.0, 2.1, 2.3, 2.4]]) - Vector([[5.0, 4.9, 4.7, 4.6]]))
print()
print(Vector([[0.0], [1.0], [2.0]]) - Vector([[3.0], [2.0], [1.0]]))
print()
print(Vector([[5.]]) - 4)
print()
print(4 - Vector([[5.]]))
print()

# print(Vector([[2.0, 2.1, 2.3, 2.4]]) - Vector([[0.0], [1.0], [2.0], [3.0]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) - Vector([[2.0, 2.1, 2.3, 2.4, 0.]]))
# print(Vector([[2.0, 2.1, 2.3, 2.4]]) - 5)
# print(5 - Vector([[2.0, 2.1, 2.3, 2.4]]))


print("\nmul\n")
v1 = Vector([[2.0, 2.1, 2.3, 2.4]])
v2 = Vector([[7.]])
print(v1 * v2)