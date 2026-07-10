import numpy as np
from scipy import stats

print("\n--- Exercise 1 ---\n")

table = np.array([[60, 140],
                  [30, 770]])
total = table.sum()

p_clicked = table[0].sum() / total
p_purchased = table[:, 0].sum() / total
p_joint = table[0, 0] / total

print(f"{'P(Clicked):':<24} {round(p_clicked, 4)}")
print(f"{'P(Purchased):':<24} {round(p_purchased, 4)}")
print(f"{'P(Purchased ∩ Clicked):':<24} {round(p_joint, 4)}")

p_purch_given_click = table[0, 0] / table[0].sum()
p_purch_given_notclick = table[1, 0] / table[1].sum()

print(f"{'P(Purchased | Clicked):':<27} {round(p_purch_given_click, 4)}")
print(f"{'P(Purchased | Not clicked):':<27} {round(p_purch_given_notclick, 4)}")

indep = abs(p_clicked * p_purchased - p_joint) < 1e-6
print(f"{'P(Clicked) * P(Purchased):':<26} {round(p_clicked * p_purchased, 4)}")
print(f"{'P(Clicked ∩ Purchased):':<26} {round(p_joint, 4)}")
print(f"independent? {'Yes' if indep else 'No'}")

table2 = np.array([[200, 300],
                   [200, 300]])
total2 = table2.sum()

p_a = table2[0].sum() / total2
p_b = table2[:, 0].sum() / total2
p_ab = table2[0, 0] / total2

indep2 = abs(p_a * p_b - p_ab) < 1e-6
print(f"{'P(A):':<11} {round(p_a, 4)}")
print(f"{'P(B):':<11} {round(p_b, 4)}")
print(f"{'P(A ∩ B):':<11} {round(p_ab, 4)}")
print(f"{'P(A) * P(B):':<11} {round(p_a * p_b, 4)}")
print(f"independent? {'Yes' if indep2 else 'No'}")

print("\n--- Exercise 2 ---\n")

p_d = 0.01
sensitivity = 0.99
specificity = 0.95
fpr = 1 - specificity

p_pos = sensitivity * p_d + fpr * (1 - p_d)
print(f"{sensitivity * p_d / p_pos:.4f}")

p_d10 = 0.10
p_pos10 = sensitivity * p_d10 + fpr * (1 - p_d10)
print(f"{sensitivity * p_d10 / p_pos10:.4f}")


def bayes_posterior(prior, sensitivity, specificity):
    fpr = 1 - specificity
    p_pos = sensitivity * prior + fpr * (1 - prior)
    return sensitivity * prior / p_pos


print(f"prevalence 1%:  {bayes_posterior(0.01, 0.99, 0.95):.4f}")
print(f"prevalence 10%: {bayes_posterior(0.10, 0.99, 0.95):.4f}")

p_neg_given_d = 1 - sensitivity
p_neg = p_neg_given_d * p_d + specificity * (1 - p_d)
print(f"{p_neg_given_d * p_d / p_neg:.6f}")

print("\n--- Exercise 3 ---\n")

joint = np.array([[0.30, 0.10, 0.05],
                  [0.10, 0.20, 0.05],
                  [0.05, 0.05, 0.10]])
weather = ["sunny", "cloudy", "rainy"]
traffic = ["light", "medium", "heavy"]

print(f"sum = {round(joint.sum(), 4)}")

p_weather = joint.sum(axis=1)
p_traffic = joint.sum(axis=0)
print(f"P(weather): {np.round(p_weather, 4)}")
print(f"P(traffic): {np.round(p_traffic, 4)}")

print(np.round(joint[0] / p_weather[0], 4))

print(np.round(joint[:, 2] / p_traffic[2], 4))

print("\n--- Exercise 4 ---\n")

rng = np.random.default_rng(seed=0)
n = 100
X0 = rng.normal(loc=[2.0, 2.0], scale=1.0, size=(n, 2))
X1 = rng.normal(loc=[-2.0, -2.0], scale=1.0, size=(n, 2))
X = np.vstack([X0, X1])
y = np.concatenate([np.zeros(n), np.ones(n)]).astype(int)

print(X.shape, y.shape)


def fit_gnb(X, y):
    model = {}
    for c in np.unique(y):
        Xc = X[y == c]
        model[int(c)] = {
            "prior": len(Xc) / len(X),
            "mean": Xc.mean(axis=0),
            "std": Xc.std(axis=0, ddof=0),
        }
    return model


model = fit_gnb(X, y)
print(f"class 0 mean: {np.round(model[0]['mean'], 4)}")
print(f"class 1 mean: {np.round(model[1]['mean'], 4)}")


def predict_gnb(X, model):
    X = np.atleast_2d(X)
    classes = sorted(model.keys())
    log_post = []
    for c in classes:
        m = model[c]
        lp = np.log(m["prior"]) + stats.norm(loc=m["mean"], scale=m["std"]).logpdf(X).sum(axis=1)
        log_post.append(lp)
    log_post = np.array(log_post)
    return np.array(classes)[np.argmax(log_post, axis=0)]


test_X = np.array([[2.0, 2.0],
                   [-2.0, -2.0],
                   [0.0, 0.0],
                   [5.0, 5.0]])
print(predict_gnb(test_X, model))

pred = predict_gnb(X, model)
print(round(np.mean(pred == y), 4))

print("\n--- Exercise 5 ---\n")

rng = np.random.default_rng(seed=0)
n = 100_000
disease = rng.random(n) < 0.01
positive = np.where(disease,
                    rng.random(n) < 0.99,
                    rng.random(n) < 0.05)
print(f"{np.sum(disease & positive) / np.sum(positive):.4f}")

rng = np.random.default_rng(seed=0)
n = 100_000
clicked = rng.random(n) < 0.20
purchased = np.where(clicked,
                     rng.random(n) < 0.30,
                     rng.random(n) < 0.0375)
print(f"{np.sum(clicked & purchased) / np.sum(clicked):.4f}")

for n in [100, 1_000, 10_000, 100_000]:
    rng = np.random.default_rng(seed=0)
    disease = rng.random(n) < 0.01
    positive = np.where(disease,
                        rng.random(n) < 0.99,
                        rng.random(n) < 0.05)
    est = np.sum(disease & positive) / np.sum(positive)
    print(f"n={n:8d}   P(D|+) = {round(est, 4)}")

estimates = []
for seed in range(30):
    rng = np.random.default_rng(seed=seed)
    n = 100_000
    disease = rng.random(n) < 0.01
    positive = np.where(disease,
                        rng.random(n) < 0.99,
                        rng.random(n) < 0.05)
    estimates.append(np.sum(disease & positive) / np.sum(positive))
print(f"SE = {np.std(estimates):.4f}")

print("\n--- Exercise 6 ---\n")


def monty_hall_trial(rng, switch):
    """Return True if the contestant wins under the given strategy."""
    car = rng.integers(low=0, high=3)
    pick = rng.integers(low=0, high=3)
    for host in range(3):
        if host != car and host != pick:
            break
    if switch:
        for final in range(3):
            if final != pick and final != host:
                break
    else:
        final = pick
    return final == car


rng = np.random.default_rng(seed=0)
stay_rate = sum(monty_hall_trial(rng, False) for _ in range(100_000)) / 100_000
print(f"stay:   {round(stay_rate, 4)}")

rng = np.random.default_rng(seed=0)
switch_rate = sum(monty_hall_trial(rng, True) for _ in range(100_000)) / 100_000
print(f"switch: {round(switch_rate, 4)}")

print(f"switch / stay = {round(switch_rate / stay_rate, 4)}")