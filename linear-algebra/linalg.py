import numpy as np 

print("\n- Exercise 1 -\n")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
d1 = np.dot(a, b)
d2 = a @ b
d3 = (a * b).sum()
print(d1, d2, d3)

m1 = np.sqrt(a @ a)
m2 = np.linalg.norm(a)

print(f"{m1:.4f} {m2:.4f}")

# cos(theta) = (a · b) / (||a|| * ||b||)
cs = d1 / (m1 * np.linalg.norm(b))
print(f"{cs:.4f}")


u = np.array([1, 0, 0]) 
v = np.array([0, 1, 0])

assert u @ v == 0

w = np.array([1, 1, 0])
print(f"u and v orthogonal: {u @ v == 0}")
print(f"u and w orthogonal: {u @ w == 0}")

print("\n- Exercise 2 -\n")

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
B = np.array([[7,  8,  9],
              [10, 11, 12]])

print(A.shape)
print(B.shape)
print(A @ B)
print((A@B).shape)

print()
print(B@A)
print((B@A).shape)

P = np.array([[1, 2],
              [3, 4]])
Q = np.array([[5, 6],
              [7, 8]])

print(P@Q)
print(Q@P)

X = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0],
              [7.0, 8.0, 9.0],
              [10.0, 11.0, 12.0]])
w = np.array([0.5, -1.0, 2.0])
y = X @ w
print(y)


print("\n- Exercise 3 -\n")

A = np.array([[2.0, 1.0], [1.0, 3.0]])
print(A.T)
print(np.eye(2))
print(np.round(np.linalg.det(A), 4))
print(np.linalg.inv(A))


A_inv = np.linalg.inv(A)
print(np.allclose(A @ A_inv, np.eye(2)))
print(np.allclose(A_inv @ A, np.eye(2)))

A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[5.0, 6.0], [7.0, 8.0]])
da = np.linalg.det(A)
db = np.linalg.det(B)
dab = np.linalg.det(A @ B)
print(int(da * db))
print(int(dab))
print(np.allclose(da * db, dab))


print((A@B).T)
print((B.T @ A.T))
print(np.allclose((A @ B).T, B.T @ A.T))


print("\n- Exercise 4 -\n")

x = np.array([3.0, -4.0, 5.0, -12.0])
print(np.linalg.norm(x, ord=1))
print(np.linalg.norm(x, ord=2))
print(np.linalg.norm(x, ord=np.inf))

M = np.array([[1.0, 2.0], [3.0, 4.0]])
print(f"{np.linalg.norm(M, ord='fro'):.4f}")
print(f"{np.sqrt(np.sum(M ** 2)):.4f}")

p1 = np.array([1.0, 2.0, 3.0])
p2 = np.array([4.0, 0.0, 5.0])

print(np.linalg.norm(p1 - p2))

v = np.array([3.0, 4.0])
v_unit = v/np.linalg.norm(v)
print(v_unit)
print(np.linalg.norm(v_unit))


print("\n- Exercise 5 -\n")

A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
b = np.array([5.0, 10.0])

x = np.linalg.solve(A, b)
print(x)

print(A @ x )
print(np.allclose(A @ x, b))
print()

A = np.array([
    [1., 1., 1.],
    [2., 1., 0.],
    [1., 3., 2.]
])

b = np.array([
    100.,
    90.,
    230.
])

x = np.linalg.solve(A, b)
print(x)

print(f"fuel: {x[0]}")
print(f"base: {x[1]}")
print(f"distance: {x[2]}")

x1 = np.linalg.solve(A, b)
x2 = np.linalg.inv(A) @ b

print(x1)
print(x2)
print(np.allclose(x1, x2))

print("\n- Exercise 6 -\n")

S = np.array([[1.0, 2.0],
              [2.0, 4.0]])

ds = np.linalg.det(S)
print(ds)

try:
    s_inv = np.linalg.inv(S)
except np.linalg.LinAlgError as e:
    print("Matrix is singular and cannot be inverted")


def safe_solve(A, b):
    if abs(np.linalg.det(A)) < 1e-10:
        return None
    return np.linalg.solve(A, b)

A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
b = np.array([5.0, 10.0])

print(safe_solve(A, b))
print(safe_solve(S, np.array([1., 2.])))


print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(S))