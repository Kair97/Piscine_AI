import numpy as np
from scipy import stats

feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
species_labels = ["setosa", "versicolor", "virginica"]


def num_header(label_w, first="species"):
    return f"{first:<{label_w}}  " + "  ".join(feature_names)


def num_row(label, values, label_w):
    cells = "  ".join(f"{v:>{len(fn)}.4f}" for v, fn in zip(values, feature_names))
    return f"{label:<{label_w}}  " + cells


print("\n--- Exercise 1 ---\n")

raw = np.genfromtxt("iris.data", delimiter=",", dtype=str)
raw = raw[raw[:, 4] != ""]
X = raw[:, :4].astype(float)
y_str = raw[:, 4]
classes, y = np.unique(y_str, return_inverse=True)

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"classes: {classes}")
print(f"counts:  {np.bincount(y)}")

print(" ".join(feature_names) + "  species")
for i in range(3):
    row = " ".join(f"{X[i, j]:>{len(feature_names[j])}}" for j in range(4))
    print(f"{row}  {y_str[i]}")

print(f"min:   {np.round(X.min(axis=0), 2)}")
print(f"max:   {np.round(X.max(axis=0), 2)}")
print(f"range: {np.round(X.max(axis=0) - X.min(axis=0), 2)}")

print("\n--- Exercise 2 ---\n")

means = X.mean(axis=0)
stds = X.std(axis=0, ddof=1)
q1 = np.percentile(X, 25, axis=0)
med = np.percentile(X, 50, axis=0)
q3 = np.percentile(X, 75, axis=0)

print(f"{'feature':<12}  {'mean':<8}{'std':<8}{'q1':<8}{'median':<8}{'q3'}")
for j in range(4):
    print(f"{feature_names[j]:<12}  {means[j]:<8.4f}{stds[j]:<8.4f}{round(q1[j], 4):<8}{round(med[j], 4):<8}{round(q3[j], 4)}")

iqr = q3 - q1
print(f"IQRs: {np.round(iqr, 4)}")
print(f"largest IQR: {feature_names[int(np.argmax(iqr))]}")

cv = stds / means
print("CV: [" + " ".join(f"{v:.4f}" for v in cv) + "]")


def outlier_count(col):
    a = np.percentile(col, 25)
    b = np.percentile(col, 75)
    spread = b - a
    return int(np.sum((col < a - 1.5 * spread) | (col > b + 1.5 * spread)))


counts = np.array([outlier_count(X[:, j]) for j in range(4)])
print(f"outliers per feature: {counts}")

print("\n--- Exercise 3 ---\n")

X_setosa = X[y_str == "Iris-setosa"]
X_versicolor = X[y_str == "Iris-versicolor"]
X_virginica = X[y_str == "Iris-virginica"]
groups = [X_setosa, X_versicolor, X_virginica]

print(f"setosa:     {X_setosa.shape}")
print(f"versicolor: {X_versicolor.shape}")
print(f"virginica:  {X_virginica.shape}")

print(num_header(11))
for label, Xg in zip(species_labels, groups):
    print(num_row(label, Xg.mean(axis=0), 11))

print(num_header(11))
for label, Xg in zip(species_labels, groups):
    print(num_row(label, Xg.std(axis=0, ddof=1), 11))

class_means = np.array([Xg.mean(axis=0) for Xg in groups])
class_stds = np.array([Xg.std(axis=0, ddof=1) for Xg in groups])
ratios = class_means.std(axis=0, ddof=1) / class_stds.mean(axis=0)
print(f"ratios: {np.round(ratios, 4)}")
print(f"most discriminative: {feature_names[int(np.argmax(ratios))]}")

print("\n--- Exercise 4 ---\n")

print(num_header(11))
for label, Xg in zip(species_labels, groups):
    print(num_row(label, stats.skew(Xg, axis=0), 11))

shapiro_p = []
print(num_header(11))
for label, Xg in zip(species_labels, groups):
    pvals = np.array([stats.shapiro(Xg[:, j]).pvalue for j in range(4)])
    shapiro_p.append(pvals)
    print(num_row(label, pvals, 11))
shapiro_p = np.array(shapiro_p)

reject = shapiro_p < 0.05
print(num_header(11))
for label, row in zip(species_labels, reject):
    cells = "  ".join(f"{str(bool(v)):>{len(fn)}}" for v, fn in zip(row, feature_names))
    print(f"{label:<11}  {cells}")

p_pw_setosa = stats.shapiro(X_setosa[:, 3]).pvalue
print(f"setosa petal_width is non-normal (Shapiro p = {round(p_pw_setosa, 4)})")

print("\n--- Exercise 5 ---\n")

corr = np.corrcoef(X, rowvar=False)
print(num_header(12, first=""))
for i, fn in enumerate(feature_names):
    print(num_row(fn, corr[i], 12))

abs_corr = np.abs(corr)
max_search = abs_corr.copy()
min_search = abs_corr.copy()
np.fill_diagonal(max_search, -np.inf)
np.fill_diagonal(min_search, np.inf)
imax = np.unravel_index(np.argmax(max_search), corr.shape)
imin = np.unravel_index(np.argmin(min_search), corr.shape)
print(f"most correlated:  {feature_names[imax[0]]} & {feature_names[imax[1]]} (corr = {round(corr[imax], 4)})")
print(f"least correlated: {feature_names[imin[0]]} & {feature_names[imin[1]]} (corr = {round(corr[imin], 4)})")

within = []
for label, Xg in zip(species_labels, groups):
    c = np.corrcoef(Xg, rowvar=False)[2, 3]
    within.append(c)
    print(f"{label:<10} petal_length × petal_width: {round(c, 4)}")

print(f"overall petal length × width corr ({round(corr[2, 3], 4)}) is much larger than the within-species correlations (max {round(max(within), 4)})")

print("\n--- Exercise 6 ---\n")

pairs = [
    ("setosa", "versicolor", X_setosa, X_versicolor),
    ("setosa", "virginica", X_setosa, X_virginica),
    ("versicolor", "virginica", X_versicolor, X_virginica),
]

all_p = []
for a_name, b_name, A, B in pairs:
    pvals = np.array([stats.ttest_ind(A[:, j], B[:, j], equal_var=False).pvalue for j in range(4)])
    all_p.extend(pvals)
    label = f"{a_name} vs {b_name}:"
    print(f"{label:<22} [" + " ".join(f"{p:.6f}" for p in pvals) + "]")

all_p = np.array(all_p)
alpha = 0.05 / 12
print(f"significant after Bonferroni (12 tests, \u03b1=0.00417): {int(np.sum(all_p < alpha))}")

res = stats.ttest_ind(X_versicolor[:, 1], X_virginica[:, 1], equal_var=False)
diff = abs(X_versicolor[:, 1].mean() - X_virginica[:, 1].mean())
print(f"sepal_width versicolor vs virginica: t = {res.statistic:.4f}  p = {res.pvalue:.4f}  |diff| = {diff:.4f}")

best = feature_names[int(np.argmax(ratios))]
worst = feature_names[int(np.argmin(ratios))]
best_within = species_labels[int(np.argmax(within))]

summary = (
    f"This exploratory analysis of the 150-flower Iris dataset identifies {best} as the most "
    f"discriminative feature, with a between-species to within-species spread ratio of "
    f"{ratios.max():.4f}, far above {worst}'s {ratios.min():.4f}. Welch two-sample t-tests separate "
    f"the three species almost perfectly: for setosa versus versicolor and setosa versus virginica, "
    f"every feature yields a p-value of essentially {0.0:.1f}, and all 12 pair-by-feature tests "
    f"remain significant after a Bonferroni correction at alpha = {alpha:.5f}. The hardest pair to "
    f"separate is sepal_width between versicolor and virginica, which still rejects with "
    f"t = {res.statistic:.4f}, p = {res.pvalue:.4f}, and an absolute mean difference of only "
    f"{diff:.4f} cm. Feature correlations look strong overall, with petal_length and petal_width "
    f"reaching {corr[2, 3]:.4f}, but this is inflated by pooling species with different means; the "
    f"largest within-species petal correlation is only {max(within):.4f}, for {best_within}, a "
    f"Simpson-paradox-like effect. Petal measurements carry most of the discriminative signal."
)
print("SUMMARY:")
print(summary)
