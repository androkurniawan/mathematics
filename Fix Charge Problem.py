import pulp as pl

# 1. Definisi problem (minimization)
model = pl.LpProblem("Fixed_Charge_Problem", pl.LpMinimize)

# 2. Variabel keputusan
x1 = pl.LpVariable("x1", lowBound=0, cat="Continuous")
x2 = pl.LpVariable("x2", lowBound=0, cat="Continuous")
x3 = pl.LpVariable("x3", lowBound=0, cat="Continuous")

y1 = pl.LpVariable("y1", cat="Binary")
y2 = pl.LpVariable("y2", cat="Binary")
y3 = pl.LpVariable("y3", cat="Binary")

# 3. Fungsi objektif
model += 200*x1 + 100*x2 + 500*x3 + 5000*y1 + 3000*y2 + 8000*y3

# 4. Kendala
model += x1 + x2 + x3 >= 100
model += x1 >= 20
model += x2 >= 30
model += x3 >= 10
model += x1 <= 50
model += x2 <= 100
model += x3 <= 30
model += 4*x1 + 2*x2 + 8*x3 <= 500

# Kendala fixed charge
model += x1 <= 50 * y1
model += x2 <= 100 * y2
model += x3 <= 30 * y3

# 5. Solve
model.solve(pl.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pl.LpStatus[model.status])
print("Nilai optimum Z =", pl.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
print("x3 =", x3.value())
print("y1 =", y1.value())
print("y2 =", y2.value())
print("y3 =", y3.value())
