import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Fixed_Charge_Problem", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Binary")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Binary")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Binary")
x4 = pulp.LpVariable("x4", lowBound=0, cat="Binary")

# 3. Fungsi objektif
model += 9*x1 + 5*x2 + 6*x3 + 4*x4

# 4. Kendala
model += 6*x1 + 3*x2 + 5*x3 + 2*x4 <= 10
model += x3 + x4 == 1
model += x3 <= x1
model += x4 <= x2

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
print("x3 =", x3.value())
print("x4 =", x4.value())
