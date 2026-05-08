import pulp
import numpy as np

# Data
D = np.array([
    [0, 120, 150, 200, 180],
    [120, 0, 160, 220, 140],
    [150, 160, 0, 130, 170],
    [200, 220, 130, 0, 110],
    [180, 140, 170, 110, 0]
])

n = len(D)
k = 5  # jumlah node yang akan dipilih

model = pulp.LpProblem("Tourist_Route", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i,j) for i in range(n) for j in range(n) if i!=j), cat='Binary')
y = pulp.LpVariable.dicts("y", (i for i in range(n)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=1, upBound=k, cat='Integer')

# Objective
model += pulp.lpSum(D[i][j] * x[(i,j)] for i in range(n) for j in range(n) if i!=j)

# Flow Conservation
for i in range(n):
    model += pulp.lpSum(x[(i,j)] for j in range(n) if i!=j) == y[i]
    model += pulp.lpSum(x[(j,i)] for j in range(n) if i!=j) == y[i]

# MTZ (diperbaiki dengan Big-M)
M = k
for i in range(n):
    for j in range(n):
        if i != j:
            model += u[i] - u[j] + M * x[(i,j)] <= M - 1 + M * (1 - y[i]) + M * (1 - y[j])

# Linking
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i,j)] <= y[i]
            model += x[(i,j)] <= y[j]

# Category
beach    = [0, 1]
cultural = [2]
mall     = [3, 4]

model += pulp.lpSum(y[i] for i in beach)    == 1
model += pulp.lpSum(y[i] for i in cultural) == 1
model += pulp.lpSum(y[i] for i in mall)     == 1

# Total node terpilih
model += pulp.lpSum(y[i] for i in range(n)) == k

# Solve
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Output
print("Status      :", pulp.LpStatus[model.status])
print("Total Jarak :", pulp.value(model.objective))

selected = [i for i in range(n) if pulp.value(y[i]) > 0.5]
route    = sorted(selected, key=lambda i: pulp.value(u[i]))

print("Node Terpilih :", selected)
print("Urutan Rute   :", route)
print("\nEdges:")
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[(i,j)]) > 0.5:
            print(f"  {i} -> {j}  (jarak: {D[i][j]})")