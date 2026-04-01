import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Fixed_Charge_Problem", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

y1 = pulp.LpVariable("y1", cat="Binary")
y2 = pulp.LpVariable("y2", cat="Binary")
y3 = pulp.LpVariable("y3", cat="Binary")

# 3. Fungsi objektif
model += 6*x1 + 4*x2 + 7*x3 - 200*y1 - 150*y2 - 100*y3

# 4. Kendala
model += 3*x1 + 2*x2 + 6*x3 <= 150
model += 4*x1 + 3*x2 + 4*x3 <= 160

# Kendala fixed charge
model += x1 <= 40*y1
model += x2 <= 53*y2
model += x3 <= 25*y3

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
print("x3 =", x3.value())
print("y1 =", y1.value())
print("y2 =", y2.value())
print("y3 =", y3.value())
