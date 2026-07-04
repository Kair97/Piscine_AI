import numpy as np 

print("\n--- Exercise 1 ---\n")
A = np.array([[4.0, 1.0],
              [2.0, 3.0]])

eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues.real)
print(eigenvectors.real)

for i in range (len(eigenvalues)):
    left = A @ eigenvectors[:, i]
    right = eigenvalues[i] * eigenvectors[:, i]

    print(left)
    print(right)
    print(np.allclose(left, right))


print()
S = np.array([[2.0, 1.0],
              [1.0, 2.0]])

vals, vecs = np.linalg.eigh(S)
print(vals)
print(np.round(vecs.T @ vecs, 10))

print("sum of eigenvalues:", eigenvalues.real.sum())
print("trace of A:", np.trace(A))


print("\n--- Exercise 2 ---\n")

A = np.array([[3.0, 1.0, 1.0],
              [-1.0, 3.0, 1.0]])

U, s, Vt = np.linalg.svd(A)
print(U.shape, s.shape, Vt.shape)
print(np.round(s, 4))

Sigma = np.zeros((2, 3))
np.fill_diagonal(Sigma, s)
A_reconstructed = U @ Sigma @ Vt

print(np.allclose(A, A_reconstructed))

U, s, Vt = np.linalg.svd(A, full_matrices=False)
print(U.shape, s.shape, Vt.shape)


print("\n--- Exercise 3 ---\n")

rng = np.random.default_rng(seed=0)

ground_truth = np.outer(rng.normal(size=10), rng.normal(size=10))

noise = rng.normal(scale=0.01, size=(10, 10))

A = ground_truth + noise

print(A.shape)
print(np.linalg.matrix_rank(A))

U, s, Vt = np.linalg.svd(A)
np.set_printoptions(precision=4, suppress=True)
print(s)

A_1 = s[0] * np.outer(U[:, 0], Vt[0, :])
error = np.linalg.norm(A - A_1, 'fro')

print(round(error, 4))

def low_rank_approx(A, k):
     U, s, Vt = np.linalg.svd(A)

     return U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]

for k in [1, 2, 5, 10]:
    A_k = low_rank_approx(A, k)
    error = np.linalg.norm(A - A_k, 'fro')
    print(f"k={k}: {error:.4f}")


print("\n--- Exercise 4 ---\n")

rng = np.random.default_rng(seed=42)

x = rng.normal(loc=0.0, scale=1.0, size=100)
y = 2.0 * x + rng.normal(loc=0.0, scale=0.5, size=100)

X = np.column_stack([x, y])

print(X.shape)

X_centered = X - X.mean(axis=0)
C_manual = (X_centered.T @ X_centered) / (X.shape[0] - 1)
print(np.round(C_manual, 4))
C_numpy = np.cov(X, rowvar=False)
print(np.round(C_numpy, 4))
print(np.allclose(C_manual, C_numpy))



print("\n--- Exercise 5 ---\n")

X_centered = X - X.mean(axis=0)
C = (X_centered.T @ X_centered) / (X.shape[0] - 1)

eigenvalues, eigenvectors = np.linalg.eigh(C)

order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
eigenvectors = eigenvectors[:, order]

print(np.round(eigenvalues, 4))
print(np.round(eigenvectors[:, 0], 4))

Z = X_centered @ eigenvectors[:, 0]

print(Z.shape)
print(np.round(Z[:5], 4))
print(round(np.var(Z, ddof=1), 4))


print("\n--- Exercise 6 ---\n")

explained = eigenvalues / eigenvalues.sum()

print(np.round(explained, 4))
print(np.round(np.cumsum(explained), 4))


def explained_variance_ratio(X, k):
    X_centered = X - X.mean(axis=0)
    C = np.cov(X_centered, rowvar=False)

    eigenvalues, _ = np.linalg.eigh(C)
    eigenvalues = np.sort(eigenvalues)[::-1]

    return eigenvalues[:k].sum() / eigenvalues.sum()


print(round(explained_variance_ratio(X, 1), 4))
print(round(explained_variance_ratio(X, 2), 4))


rng = np.random.default_rng(seed=7)
X_iso = rng.normal(loc=0.0, scale=1.0, size=(200, 2))

print(round(explained_variance_ratio(X_iso, 1), 4))