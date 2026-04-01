import pulp

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Pure_Integer_Programming_Example", pulp.LpMaximize)

# 2. Variabel keputusan
x1 = pulp.LpVariable("x1", lowBound=0, cat="Binary")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Binary")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Binary")
x4 = pulp.LpVariable("x4", lowBound=0, cat="Binary")
x5 = pulp.LpVariable("x5", lowBound=0, cat="Binary")
x6 = pulp.LpVariable("x6", lowBound=0, cat="Binary")
x7 = pulp.LpVariable("x7", lowBound=0, cat="Binary")
x8 = pulp.LpVariable("x8", lowBound=0, cat="Binary")

# 3. Fungsi objektif
model += 60*x1 + 100*x2 + 120*x3 + 90*x4 + 70*x5 + 40*x6 + 30*x7 + 20*x8

# 4. Kendala
model += 10*x1 + 20*x2 + 30*x3 + 15*x4 + 25*x5 + 5*x6 + 10*x7 + 8*x8 <= 50

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
print("x7 =", x7.value())
print("x8 =", x8.value())
