import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Pure_Integer_Programming_Example", pulp.LpMinimize)

# 2. Variabel keputusan
y1 = pulp.LpVariable("y1", lowBound=0, cat="Continous")
y2 = pulp.LpVariable("y2", lowBound=0, cat="Continous")
y3 = pulp.LpVariable("y3", lowBound=0, cat="Continous")

# 3. Fungsi objektif
model += 10*y1 + 15*y2 + 12*y3

# 4. Kendala
model += 2*y1 + y2 + 2*y3 >= 4
model += y1 + 3*y2 + 2*y3 >= 6
model += y1 + 2*y2 + y3 >= 5

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("y1 =", y1.value())
print("y2 =", y2.value())
print("y3 =", y3.value())
