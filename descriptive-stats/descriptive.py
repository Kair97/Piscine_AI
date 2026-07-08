import numpy as np
from scipy import stats

print("\n--- Exercise 1 ---\n")

ages = np.array([23, 25, 27, 29, 30, 31, 32, 32, 33, 34, 35, 38, 40, 45, 90])

print(f"mean:   {np.mean(ages):.2f}")
print(f"median: {np.median(ages):.2f}")

ages2 = ages.copy()
ages2[ages2 == 90] = 35

print(f"mean:   {np.mean(ages2):.2f}")
print(f"median: {np.median(ages2):.2f}")

result = stats.mode(ages, keepdims=False)
print(result.mode, result.count)

m = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(m.mean())
print(m.mean(axis=0))
print(m.mean(axis=1))

print("\n--- Exercise 2 ---\n")

x = np.array([2, 4, 4, 4, 5, 5, 7, 9])

print(f"population variance: {np.var(x):.4f}")
print(f"sample variance:     {np.var(x, ddof=1):.4f}")

print(f"population std: {np.std(x):.4f}")
print(f"sample std:     {np.std(x, ddof=1):.4f}")


def manual_variance(x, ddof=0):
    return ((x - x.mean()) ** 2).sum() / (len(x) - ddof)


print(np.allclose(manual_variance(x), np.var(x)))
print(np.allclose(manual_variance(x, ddof=1), np.var(x, ddof=1)))

heights_cm = np.array([165, 170, 175, 180, 185])

mean = heights_cm.mean()
std = heights_cm.std()

print(f"mean: {mean:.2f}")
print(f"std:  {std:.2f}")
print(f"range: {mean - std:.2f} to {mean + std:.2f}")

print("\n--- Exercise 3 ---\n")

x = np.arange(1, 101)

print(np.percentile(x, [25, 50, 75, 90]))
print(np.quantile(x, [0.25, 0.50, 0.75]))

rng = np.random.default_rng(seed=0)

salaries = rng.lognormal(mean=10.5, sigma=0.5, size=1000).astype(int)

print(f"p10: {int(np.percentile(salaries, 10))}")
print(f"p50: {int(np.percentile(salaries, 50))}")
print(f"p90: {int(np.percentile(salaries, 90))}")

print(f"mean:   {int(round(salaries.mean()))}")
print(f"median: {int(round(np.median(salaries)))}")
print(f"mean > median: {salaries.mean() > np.median(salaries)}")

print("\n--- Exercise 4 ---\n")

data = np.array([
    23, 25, 27, 29, 30, 31, 32, 32, 33, 34,
    35, 38, 40, 45, 90, 12, 22, 33, 36, 39
])

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(f"Q1:    {q1:.2f}")
print(f"Q3:    {q3:.2f}")
print(f"IQR:   {iqr:.2f}")
print(f"lower: {lower:.2f}")
print(f"upper: {upper:.2f}")

outliers = data[(data < lower) | (data > upper)]
print(outliers)


def iqr_outliers(x):
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return x[x < lower], x[x > upper]


lo, hi = iqr_outliers(data)

print(f"lower outliers: {lo}")
print(f"upper outliers: {hi}")

rng = np.random.default_rng(seed=42)

clean = rng.normal(loc=50.0, scale=5.0, size=200)

lo, hi = iqr_outliers(clean)

print(f"lower outliers: {len(lo)}")
print(f"upper outliers: {len(hi)}")

print("\n--- Exercise 5 ---\n")

rng = np.random.default_rng(seed=0)

normal = rng.normal(loc=0.0, scale=1.0, size=10_000)
right_skewed = rng.lognormal(mean=0.0, sigma=1.0, size=10_000)
heavy_tailed = rng.standard_t(df=3, size=10_000)

print(f"normal:        skew = {stats.skew(normal):.4f}  kurtosis = {stats.kurtosis(normal):.4f}")
print(f"right_skewed:  skew = {stats.skew(right_skewed):.4f}  kurtosis = {stats.kurtosis(right_skewed):.4f}")
print(f"heavy_tailed:  skew = {stats.skew(heavy_tailed):.4f}  kurtosis = {stats.kurtosis(heavy_tailed):.4f}")


def manual_skew(x):
    return (((x - x.mean()) / x.std()) ** 3).mean()


print(abs(manual_skew(normal) - stats.skew(normal)) < 1e-6)

print(f"mean:   {right_skewed.mean():.4f}")
print(f"median: {np.median(right_skewed):.4f}")
print(f"mean > median: {right_skewed.mean() > np.median(right_skewed)}")

print("\n--- Exercise 6 ---\n")


def summary(x):
    return {
        "count": float(len(x)),
        "mean": float(np.mean(x)),
        "std": float(np.std(x, ddof=1)),
        "min": float(np.min(x)),
        "q1": float(np.percentile(x, 25)),
        "median": float(np.median(x)),
        "q3": float(np.percentile(x, 75)),
        "max": float(np.max(x)),
    }


order = ["count", "mean", "std", "min", "q1", "median", "q3", "max"]

rng = np.random.default_rng(seed=0)

salaries = rng.lognormal(mean=10.5, sigma=0.5, size=1000).astype(int)

s_sal = summary(salaries)

for k in order:
    print(f"{k + ':':7} {s_sal[k]:.2f}")

rng = np.random.default_rng(seed=42)

normal = rng.normal(loc=100.0, scale=15.0, size=1000)

s_norm = summary(normal)

for k in order:
    print(f"{k + ':':7} {s_norm[k]:.2f}")

print(f"normal:    q3-median = {s_norm['q3'] - s_norm['median']:.2f}  median-q1 = {s_norm['median'] - s_norm['q1']:.2f}")
print(f"salaries:  q3-median = {s_sal['q3'] - s_sal['median']:.2f}  median-q1 = {s_sal['median'] - s_sal['q1']:.2f}")