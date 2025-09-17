def f(x):
    return x**3 + 2*x**2 + 10*x - 19
    # return x**2 - 6*x + 8

a = 1
b = 1.5
tol = 0.000015  #toleransi
i = 1

print("Iterasi | a       | b       | c       | f(c)")
while True:  # terus jalan sampai syarat terpenuhi
    c = (a + b) / 2
    print(f"{i:^7} | {a:.6f} | {b:.6f} | {c:.6f} | {f(c):.6f}")

    # cek apakah c adalah akarnya, jika c adalah akarnya maka stop
    if f(c) == 0:
        break
    
    # cek toleransi
    if abs(f(c)) < tol:
        break

    # update interval
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    
    i += 1