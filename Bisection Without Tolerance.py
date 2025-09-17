def f(x):
    return x**2 - 5
    # return x**2 - 9
    # return x**2 - 6*x + 8

# interval awal
a = 2
b = 3

print("Iterasi |    a     |     b    |    c     | f(c)")
for i in range(1, 4):  # banyak iterasi
    c = (a + b) / 2
    print(f"{i:^7} | {a:^7.6f} | {b:^7.6f} | {c:^7.6f} | {f(c):^7.6f}")
    
    # cek apakah c adalah akarnya, jika c adalah akarnya maka stop
    if f(c) == 0:
        break

    # cek tanda f(a)*f(c)
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c