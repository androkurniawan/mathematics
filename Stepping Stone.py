import pulp
import time
start_time = time.time()

# 1. Definisi problem (minimization)
model = pulp.LpProblem("Stepping_Stone", pulp.LpMinimize)

# 2. Variabel keputusan
x11 = pulp.LpVariable("x11", lowBound=0, cat="Integer")
x12 = pulp.LpVariable("x12", lowBound=0, cat="Integer")
x13 = pulp.LpVariable("x13", lowBound=0, cat="Integer")
x21 = pulp.LpVariable("x21", lowBound=0, cat="Integer")
x22 = pulp.LpVariable("x22", lowBound=0, cat="Integer")
x23 = pulp.LpVariable("x23", lowBound=0, cat="Integer")
x31 = pulp.LpVariable("x31", lowBound=0, cat="Integer")
x32 = pulp.LpVariable("x32", lowBound=0, cat="Integer")
x33 = pulp.LpVariable("x33", lowBound=0, cat="Integer")

# 3. Fungsi objektif
model += 20*x11 + 5*x12 + 8*x13 + 15*x21 + 20*x22 + 10*x23 + 25*x31 + 10*x32 + 19*x33

# 4. Kendala
# Kendala Supply
model += x11 + x12 + x13 == 90
model += x21 + x22 + x23 == 60
model += x31 + x32 + x33 == 50
# Kendala Demand
model += x11 + x21 + x31 == 50
model += x12 + x22 + x32 == 110
model += x13 + x23 + x33 == 40

# Kendala fixed 0*y3

# 5. Solve
model.solve(pulp.PULP_CBC_CMD(msg=False))

# 6. Hasil
print("Status:", pulp.LpStatus[model.status])
print("Nilai optimum Z =", pulp.value(model.objective))
print("x11 =", x11.value())
print("x12 =", x12.value())
print("x13 =", x13.value())
print("x21 =", x21.value())
print("x22 =", x22.value())
print("x23 =", x23.value())
print("x31 =", x31.value())
print("x32 =", x32.value())
print("x33 =", x33.value())

end_time = time.time()

print("Need", end_time - start_time, "seconds to execute the program.")