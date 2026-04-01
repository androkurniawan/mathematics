import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Pure_Integer_Programming_Example", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Binary")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Binary")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Binary")
x4 = pulp.LpVariable("x4", lowBound=0, cat="Binary")

# 3. Fungsi objektif
model += 16000*x1 + 22000*x2 + 12000*x3 + 8000*x4

# 4. Kendala
model += 5000*x1 + 7000*x2 + 4000*x3 + 3000*x4 <= 14000

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
print("x3 =", x3.value())
print("x4 =", x4.value())
