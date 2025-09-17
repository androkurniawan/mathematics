import numpy as np

def f(x):
    return np.exp(-x) - x

print("x       |    f(x)")
for i in [0.55, 0.6, 0.65, 0.7]:
    print(f"{i:^7} | {f(i):^7.6f}")