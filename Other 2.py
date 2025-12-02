import math

x = 1.90625

def f(x):
    return x**2 - math.log(x) - 3
def fa(x):
    return math.exp(x) - 4

print(f(x))
print(fa(x))