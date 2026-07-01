import time
import numpy as np


# Exercise 1
print("--- Exercise 1 ---")
a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([10.0, 20.0, 30.0, 40.0])

print(a + b)
print(b - a)
print(a * b)
print(b / a)
print(b**2)

x = np.array([1.0, 4.0, 9.0, 16.0, 25.0])
print(np.sqrt(x))
print(np.log(x))
print(np.exp(np.array([0.0, 1.0, 2.0])))

comp_a = np.array([1, 5, 3, 7, 2])
comp_b = np.array([2, 5, 1, 8, 2])
print(comp_a == comp_b)
print(comp_a > comp_b)
print(comp_a <= comp_b)

predictions = np.array([1.5, 2.0, 3.1, 4.0])
targets = np.array([1.0, 2.0, 3.0, 4.0])
mse = np.mean((predictions - targets) ** 2)
print(f"{mse:.4f}")



# Exercise 2
print("\n--- Exercise 2 ---")
broad_a = np.array([1, 2, 3, 4])
print(broad_a + 10)

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
row = np.array([100, 200, 300])
m_plus_row = m + row
print(m_plus_row)
print(m_plus_row.shape)

col = np.array([[10], [20], [30], [40]])
m_plus_col = m + col
print(m_plus_col)
print(m_plus_col.shape)

col_means = m.mean(axis=0)
print(m - col_means)

a_shape3 = np.array([1, 2, 3])
b_shape41 = np.array([[10], [20], [30], [40]])
ab_sum = a_shape3 + b_shape41
print(ab_sum)
print(ab_sum.shape)

i = np.arange(1, 11).reshape(10, 1)
j = np.arange(1, 11).reshape(1, 10)
print(i * j)



# Exercise 3
print("\n--- Exercise 3 ---")
reduction_a = np.array([4, 8, 15, 16, 23, 42])
print(reduction_a.sum())
print(reduction_a.mean())
print(reduction_a.min())
print(reduction_a.max())
print(f"{reduction_a.std():.4f}")

m_reduction = np.arange(1, 13).reshape(3, 4)
print(m_reduction)
print(m_reduction.sum())
print(m_reduction.sum(axis=0))
print(m_reduction.sum(axis=1))

print(m_reduction.mean(axis=0))
print(m_reduction.mean(axis=1))

print(m_reduction.argmax())
print(m_reduction.argmax(axis=0))
print(m_reduction.argmax(axis=1))

daily = np.array([3, 5, 2, 8, 4])
print(np.cumsum(daily))



# Exercise 4
print("\n--- Exercise 4 ---")
rng_ex4 = np.random.default_rng(42)
large_x = rng_ex4.random(1_000_000)
print(large_x.shape)


def sum_of_squares_loop(x):
    total = 0.0
    for val in x:
        total += val**2
    return total


def sum_of_squares_vec(x):
    return np.sum(x**2)


# Measure execution time across 3 loops for each strategy
loop_times = []
for _ in range(3):
    t0 = time.perf_counter()
    sum_of_squares_loop(large_x)
    t1 = time.perf_counter()
    loop_times.append((t1 - t0) * 1000.0)  # Convert to milliseconds

vec_times = []
for _ in range(3):
    t2 = time.perf_counter()
    sum_of_squares_vec(large_x)
    t3 = time.perf_counter()
    vec_times.append((t3 - t2) * 1000.0)  # Convert to milliseconds

avg_loop_time = sum(loop_times) / 3.0
avg_vec_time = sum(vec_times) / 3.0
speedup = avg_loop_time / avg_vec_time

print(f"Loop:        ~{avg_loop_time:.2f} ms")
print(f"Vectorized:  ~{avg_vec_time:.2f} ms")
print(f"Speedup:     ~{speedup:.0f}x")

# Assert mathematical equivalence matching within tiny decimal limits
assert np.isclose(sum_of_squares_loop(large_x), sum_of_squares_vec(large_x))



# Exercise 5
print("\n--- Exercise 5 ---")
nan_a = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])
print(nan_a)
print(np.isnan(nan_a))
print(nan_a.sum())
print(nan_a.mean())

print(np.nansum(nan_a))
print(np.nanmean(nan_a))
print(f"{np.nanstd(nan_a):.4f}")

replaced_nan_a = np.where(np.isnan(nan_a), np.nanmean(nan_a), nan_a)
print(replaced_nan_a)

m_nan = np.array([[1.0, 2.0, np.nan], [4.0, np.nan, 6.0], [7.0, 8.0, 9.0]])
print(np.round(np.nanmean(m_nan, axis=0), 4))
print(np.round(np.nanmean(m_nan, axis=1), 4))


# Exercise 6
print("\n--- Exercise 6 ---")
rng_ex6 = np.random.default_rng(seed=0)
u = rng_ex6.random(5)
n = rng_ex6.normal(loc=0.0, scale=1.0, size=5)
i_rand = rng_ex6.integers(low=0, high=10, size=5)

print(u)
print(n)
print(i_rand)

rng_matrix = np.random.default_rng(seed=42)
m_rand = rng_matrix.integers(low=0, high=100, size=(3, 4))
print(m_rand)

rng_normal = np.random.default_rng(seed=1)
samples = rng_normal.normal(loc=5, scale=2, size=10_000)
print(f"mean: {np.mean(samples):.2f}")
print(f"std:  {np.std(samples):.2f}")

rng_choice = np.random.default_rng(seed=7)
chosen = rng_choice.choice(np.arange(1, 11), size=5, replace=False)
print(chosen)