import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Fixed_Charge_Problem", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")

# 3. Fungsi objektif
model += 8*x1 + 5*x2

# 4. Kendala
model += x1 + x2 <= 6
model += 9*x1 + 5*x2 <= 45

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
