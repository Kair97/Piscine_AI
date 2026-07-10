import numpy as np
from scipy import stats
rng = np.random.default_rng(seed=0)
print(rng.integers(low=0, high=2, size=10))