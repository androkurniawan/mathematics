import math

def f(x):
    return math.exp(x) - 4*x - 1

def ff(x):
    return math.exp(x) - 4

x = 0

print(f(x))
print(ff(x))
print("nilai x terbaru =", x - (f(x)/ff(x)))