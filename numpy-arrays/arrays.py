import numpy as np

print("\n--- Exercise 0 ---\n")
print(np.__version__)

print("\n=====================================================")


print("\n--- Exercise 1 ---\n")
a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.zeros(10)
print(b)

c = np.ones(5, dtype=int)
print(c)

d = np.arange(10)
print(d)

e = np.linspace(0, 1, 11)
print(e)

m = np.full((3, 4), 7)
print(m)

np.random.seed(42)

r = np.random.rand(5)
print(r)

i = np.eye(2, 3)
print(i)



print("\n--- Exercise 2 ---\n")

x = np.arange(12)
print(x.shape, x.dtype, x.ndim, x.size)

y = x.reshape(3, 4)
print(y)
print(y.shape)

z = x.reshape(2, 2, 3)
print(z)
print(z.shape)

auto = x.reshape(4, -1)
print(auto.shape)

fl = x.astype(np.float64)
print(fl.dtype)
i8 = x.astype(np.int8)
print(i8.dtype)


print(y.T)
print(y.T.shape)

flat_y = y.flatten()
print(flat_y,"\n",flat_y.shape, flat_y.dtype)


print("\n--- Exercise 3 ---\n")

a = np.arange(10)
print(a)
print(a[0])
print(a[-1])
print(a[2:5])
print(a[::2])
print(a[::-1])

m = np.arange(1, 13).reshape(3, 4)
print(m.shape)
print(m)
print(m[0])
print(m[:, 0])
print(m[1, 2])
print(m[0:2, 1:3])

m[1] = 0
print(m)
m = np.arange(1, 13).reshape(3, 4)
s = m[:, 1:3]
s[0, 0] = 99
print(s)
print(m)
# The original m was modified because slicing creates a view referencing the exact same memory allocation block.


print("\n--- Exercise 4 ---\n")

a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(a[[0, 3, 7]])

rev = np.arange(len(a)-1, -1, -1)
print(a[rev])

m = np.arange(1, 13).reshape(3, 4)

print(m)
print(m[[0, 2]])
print(m[[0, 1, 2], [1, 3, 0]])

print("\n--- Exercise 5 ---\n")
a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
mask = a > 4
print(mask)
print(a[mask])

comb = (a >= 3) & (a <= 6)
print(a[comb])

a[mask] = 0
print(a)

temps = np.array([21.5, 19.0, 25.7, 30.1, 17.8, 22.3, 28.4, 33.0])
form_temps = np.where(temps > 25, "hot", "cold")
print(form_temps)

print("\n--- Exercise 6 ---\n")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

cont = np.concatenate([a, b])
print(cont)

stack = np.stack([a, b])
print(stack)
print(stack.shape)

hps = np.hstack([a, b])
print(hps)
print(hps.shape)

vs = np.vstack([a, b])
print(vs)
print(vs.shape)

m1 = np.arange(1, 7).reshape(2, 3)
m2 = np.arange(7, 13).reshape(2, 3)

print(np.vstack([m1, m2]))
print(np.vstack([m1, m2]).shape)
print(np.hstack([m1, m2]))
print(np.hstack([m1, m2]).shape)

feature1 = np.array([1.1, 2.2, 3.3])
feature2 = np.array([10.0, 20.0, 30.0])
feature3 = np.array([100, 200, 300])

cmm = np.vstack([feature1, feature2, feature3]).T
print(cmm)