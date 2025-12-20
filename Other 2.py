import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Fixed_Charge_Problem", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Continous")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Continous")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Continous")

# 3. Fungsi objektif
model += 4*x1 + 6*x2 + 5*x3

# 4. Kendala
model += 2*x1 + x2 + x3 <= 10
model += x1 + 3*x2 + 2*x3 <= 15
model += 2*x1 + 2*x2 + x3 <= 12

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
print("x3 =", x3.value())
