import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Fixed_Charge_Problem", pulp.LpMinimize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Binary")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Binary")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Binary")
x4 = pulp.LpVariable("x4", lowBound=0, cat="Binary")
x5 = pulp.LpVariable("x5", lowBound=0, cat="Binary")
x6 = pulp.LpVariable("x6", lowBound=0, cat="Binary")

# 3. Fungsi objektif
model += x1 + x2 + x3 + x4 + x5 + x6

# 4. Kendala
model += x1 + x2 >= 1
model += x1 + x2 + x6 >= 1
model += x3 + x4 >= 1
model += x3 + x4 + x5 >= 1
model += x4 + x5 + x6 >= 1
model += x2 + x5 + x6 >= 1

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x1 =", x1.value())
print("x2 =", x2.value())
print("x3 =", x3.value())
print("x4 =", x4.value())
print("x5 =", x5.value())
print("x6 =", x6.value())
