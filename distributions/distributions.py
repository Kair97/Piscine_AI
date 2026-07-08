import numpy as np
from scipy import stats

np.set_printoptions(linewidth=200)

print("\n--- Exercise 1 ---\n")

iq = stats.norm(loc=100, scale=15)

print(f"{iq.pdf(100):.4f}")
print(f"{iq.cdf(100):.4f}")
print(f"{iq.cdf(115):.4f}")

print(f"{iq.cdf(115) - iq.cdf(85):.4f}")

print(f"{iq.ppf(0.95):.2f}")

z = stats.norm(loc=0, scale=1)

print(f"{z.cdf(1) - z.cdf(-1):.4f}")
print(f"{z.cdf(2) - z.cdf(-2):.4f}")
print(f"{z.cdf(3) - z.cdf(-3):.4f}")

print("\n--- Exercise 2 ---\n")

coin = stats.binom(n=10, p=0.5)

print(f"{coin.pmf(5):.4f}")
print(f"{coin.cdf(5):.4f}")
print(f"{1 - coin.cdf(6):.4f}")

ks = np.arange(0, 11)
print(np.round(coin.pmf(ks), 4))

print(f"mean: {coin.mean()}   formula: {10 * 0.5}")
print(f"var:  {coin.var()}   formula: {10 * 0.5 * (1 - 0.5)}")

print(f"{stats.binom(n=200, p=0.02).cdf(5):.4f}")

print("\n--- Exercise 3 ---\n")

print(round((130 - 100) / 15, 4))
print(round((90 - 100) / 15, 4))

print(f"{stats.norm.cdf(2.0) * 100:.2f}")

print(f"{stats.norm.ppf(0.8) * 15 + 100:.2f}")

heights_cm = np.array([165, 170, 175, 180, 185])
print(np.round((heights_cm - heights_cm.mean()) / heights_cm.std(ddof=0), 4))

print("\n--- Exercise 4 ---\n")

rng = np.random.default_rng(seed=0)
for n in [100, 1_000, 100_000]:
    sample = rng.normal(loc=0.0, scale=1.0, size=n)
    print(f"n={n:6d}  mean={sample.mean():.4f}  std={sample.std(ddof=1):.4f}")


def ecdf(sample):
    x_sorted = np.sort(sample)
    F = np.arange(1, len(sample) + 1) / len(sample)
    return x_sorted, F


rng = np.random.default_rng(seed=42)
sample = rng.normal(loc=0.0, scale=1.0, size=1000)
x_sorted, F = ecdf(sample)

print(f"x at F=0.5: {x_sorted[499]:.4f}")
print(f"F at index 499: {F[499]}")

rng = np.random.default_rng(seed=42)
sample = rng.normal(loc=0.0, scale=1.0, size=10_000)
empirical = np.mean(sample <= 1.0)

print(f"empirical:   {empirical:.4f}")
print(f"theoretical: {stats.norm.cdf(1.0):.4f}")

sample = stats.norm.rvs(loc=5, scale=2, size=1000, random_state=0)

print(f"mean: {sample.mean():.4f}")
print(f"std:  {sample.std(ddof=1):.4f}")

print("\n--- Exercise 5 ---\n")

rng = np.random.default_rng(seed=0)
single_samples = rng.exponential(scale=1.0, size=10_000)

print(f"mean: {single_samples.mean():.4f}")
print(f"std:  {single_samples.std(ddof=1):.4f}")
print(f"skew: {stats.skew(single_samples):.4f}")

rng = np.random.default_rng(seed=0)
sample_means = rng.exponential(scale=1.0, size=(10_000, 30)).mean(axis=1)

print(f"mean: {sample_means.mean():.4f}")
print(f"std:  {sample_means.std(ddof=1):.4f}")
print(f"skew: {stats.skew(sample_means):.4f}")

rng = np.random.default_rng(seed=0)
sample_means_large = rng.exponential(scale=1.0, size=(10_000, 300)).mean(axis=1)

print(f"mean: {sample_means_large.mean():.4f}")
print(f"std:  {sample_means_large.std(ddof=1):.4f}")
print(f"skew: {stats.skew(sample_means_large):.4f}")

for n in [1, 30, 300]:
    print(f"{f'n={n}:':<6} {1 / np.sqrt(n):.4f}")

print("\n--- Exercise 6 ---\n")

rng = np.random.default_rng(seed=0)
normal_sample = rng.normal(loc=0.0, scale=1.0, size=200)
exp_sample = rng.exponential(scale=1.0, size=200)

W_normal, p_normal = stats.shapiro(normal_sample)
W_exp, p_exp = stats.shapiro(exp_sample)

print(f"normal_sample:  W={W_normal:.4f}  p={p_normal:.4f}")
print(f"exp_sample:     W={W_exp:.4f}  p={p_exp:.4f}")

print(f"normal_sample:  normal at \u03b1=0.05? {'Yes' if p_normal >= 0.05 else 'No'}")
print(f"exp_sample:     normal at \u03b1=0.05? {'Yes' if p_exp >= 0.05 else 'No'}")

rng = np.random.default_rng(seed=0)
avg_sample = rng.exponential(scale=1.0, size=(200, 30)).mean(axis=1)
W, p = stats.shapiro(avg_sample)

print(f"W={W:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

rng = np.random.default_rng(seed=0)
small_exp = rng.exponential(scale=1.0, size=30)
W, p = stats.shapiro(small_exp)

print(f"W={W:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")