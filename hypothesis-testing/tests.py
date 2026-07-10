import numpy as np
from scipy import stats

print("\n--- Exercise 1 ---\n")

rng = np.random.default_rng(seed=0)
n = 200
x = rng.normal(loc=0.0, scale=1.0, size=n)
y = 0.7 * x + rng.normal(loc=0.0, scale=0.5, size=n)

r, p = stats.pearsonr(x, y)
print(f"r={r:.4f}  p={p:.4f}")

print(f"reject null at \u03b1=0.05? {'Yes' if p < 0.05 else 'No'}")

rho, p = stats.spearmanr(x, y)
print(f"rho={rho:.4f}  p={p:.4f}")

rng = np.random.default_rng(seed=1)
x = np.linspace(1, 100, 200)
y = np.log(x) + rng.normal(loc=0.0, scale=0.05, size=200)

r, _ = stats.pearsonr(x, y)
rho, _ = stats.spearmanr(x, y)
print(f"pearson:  {r:.4f}")
print(f"spearman: {rho:.4f}")

print("\n--- Exercise 2 ---\n")

rng = np.random.default_rng(seed=0)
weights = rng.normal(loc=99.5, scale=2.0, size=30)

result = stats.ttest_1samp(weights, popmean=100.0)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

rng = np.random.default_rng(seed=0)
weights_large = rng.normal(loc=99.5, scale=2.0, size=300)

result = stats.ttest_1samp(weights_large, popmean=100.0)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

result = stats.ttest_1samp(weights_large, popmean=100.0, alternative="less")
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

mean = weights_large.mean()
std_sample = weights_large.std(ddof=1)
manual_t = (mean - 100.0) / (std_sample / np.sqrt(len(weights_large)))
print(f"manual t = {manual_t:.4f}")

print("\n--- Exercise 3 ---\n")

rng = np.random.default_rng(seed=0)
variant_a = rng.normal(loc=10.0, scale=2.0, size=200)
variant_b = rng.normal(loc=10.5, scale=2.0, size=200)

result = stats.ttest_ind(variant_a, variant_b, equal_var=False)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

result = stats.ttest_ind(variant_a, variant_b, equal_var=True)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

rng = np.random.default_rng(seed=1)
group_x = rng.normal(loc=0.0, scale=1.0, size=30)
group_y = rng.normal(loc=0.5, scale=5.0, size=200)

p_student = stats.ttest_ind(group_x, group_y, equal_var=True).pvalue
p_welch = stats.ttest_ind(group_x, group_y, equal_var=False).pvalue
print(f"Student p={p_student:.4f}")
print(f"Welch   p={p_welch:.4f}")

n_a = len(variant_a)
n_b = len(variant_b)
var_a = variant_a.var(ddof=1)
var_b = variant_b.var(ddof=1)
pooled_std = np.sqrt(((n_a - 1) * var_a + (n_b - 1) * var_b) / (n_a + n_b - 2))
d = (variant_b.mean() - variant_a.mean()) / pooled_std
print(f"Cohen's d = {d:.4f}")

print("\n--- Exercise 4 ---\n")

rng = np.random.default_rng(seed=0)
n = 25
before = rng.normal(loc=140.0, scale=10.0, size=n)
after = before - rng.normal(loc=5.0, scale=3.0, size=n)

result = stats.ttest_rel(before, after)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

result = stats.ttest_ind(before, after, equal_var=False)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

paired = stats.ttest_rel(before, after)
one_sample = stats.ttest_1samp(before - after, popmean=0.0)
print(f"paired:        t={paired.statistic:.4f}  p={paired.pvalue:.4f}")
print(f"one-sample on diff: t={one_sample.statistic:.4f}  p={one_sample.pvalue:.4f}")

rng = np.random.default_rng(seed=42)
n = 25
before = rng.normal(loc=140.0, scale=10.0, size=n)
after = before + rng.normal(loc=0.0, scale=3.0, size=n)

result = stats.ttest_rel(before, after)
t = result.statistic
p = result.pvalue
print(f"t={t:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

print("\n--- Exercise 5 ---\n")

observed = np.array([89, 110, 96, 108, 105, 92])
expected = np.array([100, 100, 100, 100, 100, 100])

result = stats.chisquare(observed, expected)
chi2 = result.statistic
p = result.pvalue
print(f"chi2={chi2:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

rng = np.random.default_rng(seed=0)
rolls = rng.choice([1, 2, 3, 4, 5, 6], size=600, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.25])
observed = np.bincount(rolls, minlength=7)[1:]
expected = np.full(6, 100)

result = stats.chisquare(observed, expected)
chi2 = result.statistic
p = result.pvalue
print(f"chi2={chi2:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")


def manual_chi2(observed, expected):
    return ((observed - expected) ** 2 / expected).sum()


print(f"manual chi2 = {manual_chi2(observed, expected):.4f}")

observed = np.array([480, 320, 150, 50])
expected = 1000 * np.array([0.5, 0.3, 0.15, 0.05])

result = stats.chisquare(observed, expected)
chi2 = result.statistic
p = result.pvalue
print(f"chi2={chi2:.4f}  p={p:.4f}  reject? {'Yes' if p < 0.05 else 'No'}")

print("\n--- Exercise 6 ---\n")

table = np.array([[90, 30],
                  [60, 20],
                  [40, 60]])

chi2, p, dof, expected = stats.chi2_contingency(table)
print(f"chi2={chi2:.4f}  p={p:.4f}  dof={dof}  reject? {'Yes' if p < 0.05 else 'No'}")

print(np.round(expected, 2))

rng = np.random.default_rng(seed=0)
row_marginals = np.array([100, 150, 200])
col_p = np.array([0.4, 0.6])
table_indep = np.array([rng.multinomial(n, col_p) for n in row_marginals])

chi2, p, dof, expected = stats.chi2_contingency(table_indep)
print(f"chi2={chi2:.4f}  p={p:.4f}  dof={dof}  reject? {'Yes' if p < 0.05 else 'No'}")

chi2, p, dof, expected = stats.chi2_contingency(table)
n = table.sum()
r, c = table.shape
V = np.sqrt(chi2 / (n * (min(r, c) - 1)))
print(f"Cramer's V = {V:.4f}")