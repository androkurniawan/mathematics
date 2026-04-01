import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Fixed_Charge_Problem", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")
x4 = pulp.LpVariable("x4", lowBound=0, cat="Integer")
x5 = pulp.LpVariable("x5", lowBound=0, cat="Integer")

y1 = pulp.LpVariable("y1", cat="Binary")
y2 = pulp.LpVariable("y2", cat="Binary")
y3 = pulp.LpVariable("y3", cat="Binary")
y4 = pulp.LpVariable("y4", cat="Binary")
y5 = pulp.LpVariable("y5", cat="Binary")

# 3. Fungsi objektif
model += 25*x1 + 20*x2 + 23*x3 + 14*x4 + 18*x5 - 80000*y1 - 50000*y2 - 60000*y3 - 30000*y4 - 40000*y5

# 4. Kendala
model += x1 <= 5000
model += x2 <= 4000
model += x3 <= 3000
model += x4 <= 4000
model += x5 <= 3000
model += x1 + x2 + x3 + x4 + x5 <= 10000

# Kendala fixed charge
model += x1 <= 5000*y1
model += x2 <= 4000*y2
model += x3 <= 3000*y3
model += x4 <= 4000*y4
model += x5 <= 3000*y5

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
print("y1 =", y1.value())
print("y2 =", y2.value())
print("y3 =", y3.value())
print("y4 =", y4.value())
print("y5 =", y5.value())
