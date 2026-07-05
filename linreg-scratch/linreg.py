import numpy as np

print("\n--- Exercise 1 ---\n")
rng = np.random.default_rng(seed=0)
n = 100
x = rng.uniform(low=-5.0, high=5.0, size=n)
y = 2.0 * x + 1.0 + rng.normal(loc=0.0, scale=1.0, size=n)

print(x.shape, y.shape)
print("mean(x) =", round(x.mean(), 4))
print("mean(y) =", round(y.mean(), 4))

corr = np.corrcoef(x, y)[0, 1]
print(round(corr, 4))


print("\n--- Exercise 2 ---\n")

def predict(x, w, b):
    """Return the model's predictions for inputs x."""
    return w * x + b


def mse_loss(x, y, w, b):
    """Return the mean-squared-error of predict(x, w, b) against y."""
    y_pred = predict(x, w, b)
    return np.mean((y - y_pred) ** 2)

print(round(mse_loss(x, y, w=0.0, b=0.0), 4))

print(round(mse_loss(x, y, w=2.0, b=1.0), 4))

losses = []

for w in np.linspace(0.0, 4.0, 11):
    losses.append(mse_loss(x, y, w, b=1.0))

print(round(min(losses), 4))


print("\n--- Exercise 3 ---\n")

def gradients(x, y, w, b):
    """Return (dL/dw, dL/db) as a tuple of two scalars."""
    y_pred = predict(x, w, b)
    error = y - y_pred

    dw = -2 * np.mean(x * error)
    db = -2 * np.mean(error)

    return dw, db

dw, db = gradients(x, y, w=2.0, b=1.0)

print("dL/dw =", round(dw, 4))
print("dL/db =", round(db, 4))

dw, db = gradients(x, y, w=0.0, b=0.0)

print("dL/dw =", round(dw, 4))
print("dL/db =", round(db, 4))

h = 1e-5

analytical_dw, _ = gradients(x, y, w=1.0, b=0.5)

numerical_dw = (
    mse_loss(x, y, w=1.0 + h, b=0.5)
    - mse_loss(x, y, w=1.0 - h, b=0.5)
) / (2 * h)

print("analytical dL/dw =", round(analytical_dw, 6))
print("numerical  dL/dw =", round(numerical_dw, 6))


print("\n---Exercise 4 ---\n")

def gradient_descent(x, y, lr=0.01, n_iter=1000, w0=0.0, b0=0.0):
    """
    Run gradient descent for n_iter steps starting from (w0, b0) with
    learning rate lr. Return (w, b, loss_history) where loss_history is
    a 1D NumPy array of length n_iter+1 (loss at iteration 0, 1, ..., n_iter).
    """
    w = w0
    b = b0

    loss_history = [mse_loss(x, y, w, b)]

    for _ in range(n_iter):
        dw, db = gradients(x, y, w, b)

        w = w - lr * dw
        b = b - lr * db

        loss_history.append(mse_loss(x, y, w, b))

    return w, b, np.array(loss_history)


w, b, loss_history = gradient_descent(x, y)

print(f"iter    0: loss = {loss_history[0]:.4f}")
print(f"iter  100: loss = {loss_history[100]:.4f}")
print(f"iter  500: loss = {loss_history[500]:.4f}")
print(f"iter 1000: loss = {loss_history[1000]:.4f}")

print(f"final w = {w:.4f}")
print(f"final b = {b:.4f}")


for lr in [0.001, 0.01, 0.1]:
    _, _, loss_history = gradient_descent(x, y, lr=lr, n_iter=100)
    print(f"lr={lr:<6} final loss = {loss_history[-1]:.4f}")



print("\n---Exercise 5 ---\n")

rng = np.random.default_rng(seed=42)

n, d = 200, 3

X = rng.uniform(low=-1.0, high=1.0, size=(n, d))

true_w = np.array([1.5, -2.0, 0.5])
true_b = 0.7

y = X @ true_w + true_b + rng.normal(loc=0.0, scale=0.1, size=n)

print(X.shape, y.shape, true_w.shape)


def predict_multi(X, w, b):
    return X @ w + b


def mse_loss_multi(X, y, w, b):
    y_pred = predict_multi(X, w, b)
    return np.mean((y - y_pred) ** 2)


def gradients_multi(X, y, w, b):
    """Return (dL/dw, dL/db) where dL/dw has shape (d,) and dL/db is a scalar."""
    y_pred = predict_multi(X, w, b)
    error = y - y_pred

    dw = -2 * np.mean(X * error[:, np.newaxis], axis=0)
    db = -2 * np.mean(error)

    return dw, db


def gradient_descent_multi(X, y, lr=0.05, n_iter=2000, w0=None, b0=0.0):
    if w0 is None:
        w = np.zeros(X.shape[1])
    else:
        w = w0.copy()

    b = b0

    loss_history = [mse_loss_multi(X, y, w, b)]

    for _ in range(n_iter):
        dw, db = gradients_multi(X, y, w, b)

        w = w - lr * dw
        b = b - lr * db

        loss_history.append(mse_loss_multi(X, y, w, b))

    return w, b, np.array(loss_history)


w_gd, b_gd, loss_history = gradient_descent_multi(X, y)

print(f"iter    0: loss = {loss_history[0]:.4f}")
print(f"iter  500: loss = {loss_history[500]:.4f}")
print(f"iter 1000: loss = {loss_history[1000]:.4f}")
print(f"iter 2000: loss = {loss_history[2000]:.4f}")

print("final w =", np.round(w_gd, 4))
print(f"final b = {b_gd:.4f}")


print("\n---Exercise 6 ---\n")

X_aug = np.hstack([X, np.ones((X.shape[0], 1))])

print(X_aug.shape)

w_hat = np.linalg.solve(X_aug.T @ X_aug, X_aug.T @ y)

print(np.round(w_hat, 4))

print(np.allclose(w_hat[:d], w_gd, atol=1e-3))
print(np.isclose(w_hat[d], b_gd, atol=1e-3))

w = w_hat[:d]
b = w_hat[d]

print(round(mse_loss_multi(X, y, w, b), 4))