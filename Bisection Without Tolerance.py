def f(x):
    # return x**2 - 5
    return x**2 - 9
    # return 23*x**7 - 125*x**6 + 120*x**4 - 15*x**3 + 120*x**2 - 3

# interval awal
a = -4
b = 3

if f(a) * f(b) > 0:
        print("Tidak bisa dilanjutkan, silahkan ubah batasnya sehingga f(a)*f(b) < 0")
elif f(a) == 0:
    print("Akarnya adalah =", a)
elif f(b) == 0:
     print("Akarnya adalah =", b)
else:
    print("Iterasi |    a     |     b    |    c     | f(c)")
    for i in range(1, 20):  # banyak iterasi
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