import numpy as np
from scipy import stats
result = stats.ttest_1samp([1, 2, 3, 4, 5], popmean=3.0)
print(f"t={result.statistic:.4f}  p={result.pvalue:.4f}")