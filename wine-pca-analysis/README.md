# Wine PCA Analysis

A NumPy-only raid: a set of vectorized matrix puzzles (with a pytest suite) and a
from-scratch PCA analysis of the UCI Wine dataset. No scikit-learn, no Pandas.

## Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv ex00
source ex00/bin/activate        # Windows: ex00\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the puzzle tests
pytest test_puzzles.py -v

# 4. Run the Wine analysis
python3 wine.py

# 5. Deactivate when finished
deactivate
```

## Files

- `puzzles.py` — five vectorized matrix functions (`rotate_90`, `transpose_no_T`,
  `is_magic_square`, `block_trace`, `top_k_indices`), no Python loops over elements.
- `test_puzzles.py` — 17 pytest cases (positive, negative, and edge cases).
- `wine.py` — loads `wine.data`, standardizes features, and runs PCA from scratch.
- `wine.data` — UCI Wine dataset (178 samples, 1 label + 13 features).

## Analysis summary

We loaded the 178-sample UCI Wine dataset with `np.genfromtxt`, split the integer
class label from the 13 chemical features, and standardized every feature to zero
mean and unit variance — a necessary step because the `proline` feature spans the
hundreds while most others sit below 5, so without scaling it would dominate the
variance. We confirmed that the covariance matrix of the standardized data (with
`ddof=0`) has trace 13.0 and equals the correlation matrix of the raw data. Running
PCA via `np.linalg.eigh` of the covariance matrix, the first component explains about
36% of the variance and the second about 19%. Reading the cumulative variance, the
first **5 components** are needed to reach at least 80% of total variance, and **10
components** to reach 95%. Projecting onto the top two components separates the three
cultivars clearly: class 1 sits at `[-2.2827, -0.9679]`, class 2 at `[0.0390, 1.6435]`,
and class 3 at `[2.7482, -1.2413]`. The class means are well apart in the 2D plane, so
the wines of the three cultivars are indeed distinguishable along just a small number
of principal components — the answer procurement asked for.
