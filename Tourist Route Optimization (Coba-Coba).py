import pulp
import numpy as np

# =========================
# DATA (5 DESTINASI)
# =========================

D = np.array([
    [0, 120, 150, 200, 180],
    [120, 0, 160, 220, 140],
    [150, 160, 0, 130, 170],
    [200, 220, 130, 0, 110],
    [180, 140, 170, 110, 0]
])

n = len(D)

# =========================
# MODEL
# =========================

model = pulp.LpProblem("Tourist_Route", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i,j) for i in range(n) for j in range(n) if i!=j), cat='Binary')
y = pulp.LpVariable.dicts("y", (i for i in range(n)), cat='Binary')
# u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=1, upBound=n, cat='Integer')

# =========================
# OBJECTIVE
# =========================

model += pulp.lpSum(D[i][j] * x[(i,j)] for i in range(n) for j in range(n) if i!=j)

# =========================
# FLOW CONSERVATION
# =========================

for i in range(n):
    model += pulp.lpSum(x[(i,j)] for j in range(n) if i!=j) == y[i]
    model += pulp.lpSum(x[(j,i)] for j in range(n) if i!=j) == y[i]

# =========================
# MTZ
# =========================

# for i in range(n):
#     for j in range(n):
#         if i != j:
#             model += u[i] - u[j] + n*x[(i,j)] <= n-1

# =========================
# LINKING
# =========================

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i,j)] <= y[i]
            model += x[(i,j)] <= y[j]

# =========================
# CATEGORY (VERSI SEDERHANA)
# =========================

# Misal:
# 0,1 = Beach
# 2 = Cultural
# 3,4 = Mall

# beach = [0,1]
# cultural = [2]
# mall = [3,4]

# Constraint:
# model += pulp.lpSum(y[i] for i in beach) == 1
# model += pulp.lpSum(y[i] for i in cultural) == 1
# model += pulp.lpSum(y[i] for i in mall) == 1

# =========================
# SOLVE
# =========================

model.solve(pulp.PULP_CBC_CMD(msg=1))

# =========================
# OUTPUT
# =========================

print("Status:", pulp.LpStatus[model.status])
print("Total Distance:", pulp.value(model.objective))

selected = [i for i in range(n) if pulp.value(y[i]) == 1]
# route = sorted(selected, key=lambda i: pulp.value(u[i]))

print("\nSelected Nodes:", selected)
# print("Route Order:", route)

print("\nEdges:")
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[(i,j)]) == 1:
            print(f"{i} -> {j}")