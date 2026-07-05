from __future__ import annotations

import numpy as np


def standardize(X: np.ndarray) -> np.ndarray:     
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    return (X - mean) / std


def pca(X: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    n = X.shape[0]
    Xc = X - X.mean(axis=0)
    cov = (Xc.T @ Xc) / n  # ddof=0, совпадает с np.cov(X, rowvar=False, ddof=0)

    eigvals, eigvecs = np.linalg.eigh(cov)  # eigh: возрастающий порядок
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    total_variance = eigvals.sum()
    explained_variance_ratio = eigvals[:k] / total_variance
    projection = Xc @ eigvecs[:, :k]
    return projection, explained_variance_ratio


def main() -> None:
    data = np.genfromtxt("wine.data", delimiter=",")
    y = data[:, 0].astype(int)
    X = data[:, 1:]

    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")
    classes, counts = np.unique(y, return_counts=True)
    print(f"classes: {classes}")
    print(f"counts:  {counts}")
    print(f"feature means:\n{np.round(X.mean(axis=0), 4)}")
    print(f"feature stds:\n{np.round(X.std(axis=0), 4)}")

    X_std = standardize(X)
    print(f"\nX_std column means ~0: {np.allclose(X_std.mean(axis=0), 0, atol=1e-8)}")
    print(f"X_std column stds ~1: {np.allclose(X_std.std(axis=0), 1)}")

    cov = np.cov(X_std, rowvar=False, ddof=0)
    print(f"cov(X_std) shape: {cov.shape}, trace: {np.trace(cov):.4f}")

    corr = np.corrcoef(X, rowvar=False)
    print(f"cov(X_std, ddof=0) == corr(X): {np.allclose(cov, corr)}")

    _, evr = pca(X_std, k=13)
    print(f"\nexplained variance ratios:\n{np.round(evr, 4)}")
    print(f"sum of ratios: {evr.sum():.4f}")

    cumvar = np.cumsum(evr)
    k80 = int(np.argmax(cumvar >= 0.80) + 1)
    k95 = int(np.argmax(cumvar >= 0.95) + 1)
    print(f"cumulative variance:\n{np.round(cumvar, 4)}")
    print(f"components for >=80% variance: {k80}")
    print(f"components for >=95% variance: {k95}")

    proj2, _ = pca(X_std, k=2)
    print(f"\nprojection shape: {proj2.shape}")
    for c in classes:
        class_mean = proj2[y == c].mean(axis=0)
        print(f"class {c} mean: {np.round(class_mean, 4)}")


if __name__ == "__main__":
    main()