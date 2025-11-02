# tsp_pulp_mtz.py
# PuLP TSP example with MTZ subtour elimination
# 4-city example: 1=A, 2=B, 3=C, 4=D

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpStatus, value, PULP_CBC_CMD

# Data: cities and distance matrix
cities = [1,2,3,4]  # 1=A, 2=B, 3=C, 4=D
d = {
    (1,2):10, (1,3):15, (1,4):20,
    (2,1):10, (2,3):35, (2,4):25,
    (3,1):15, (3,2):35, (3,4):30,
    (4,1):20, (4,2):25, (4,3):30
}

n = len(cities)

# Problem
prob = LpProblem("TSP_4cities_MTZ", LpMinimize)

# Decision variables x[i,j] (binary) for i != j
x = {}
for i in cities:
    for j in cities:
        if i != j:
            x[(i,j)] = LpVariable(f"x_{i}_{j}", cat=LpBinary)

# MTZ variables u_i (continuous) used to eliminate subtours
u = {}
for i in cities:
    # u in [1, n]
    u[i] = LpVariable(f"u_{i}", lowBound=1, upBound=n, cat='Continuous')

# Objective: minimize total distance
prob += lpSum(d[(i,j)] * x[(i,j)] for i in cities for j in cities if i != j), "TotalDistance"

# Degree constraints: exactly one outgoing and one incoming for each city
for i in cities:
    prob += lpSum(x[(i,j)] for j in cities if i != j) == 1, f"Out_{i}"
for j in cities:
    prob += lpSum(x[(i,j)] for i in cities if i != j) == 1, f"In_{j}"

# MTZ subtour elimination constraints
# Fix u_1 = 1 to set a reference (city 1 is origin)
prob += u[1] == 1, "u_1_fixed"
# For all i != j: u_i - u_j + n*x_ij <= n-1
for i in cities:
    for j in cities:
        if i != j:
            prob += u[i] - u[j] + n * x[(i,j)] <= n - 1, f"MTZ_{i}_{j}"

# Solve
solver = PULP_CBC_CMD(msg=True)  # set msg=False to suppress solver output
prob.solve(solver)

# Output results
print("Status:", LpStatus[prob.status])
print("Objective (total distance) =", value(prob.objective))
print("\nSelected arcs (x_ij = 1):")
selected = []
for i,j in x:
    if value(x[(i,j)]) > 0.5:
        print(f"  {i} -> {j} (d={d[(i,j)]})")
        selected.append((i,j))

print("\nu values:")
for i in cities:
    print(f"  u_{i} = {value(u[i])}")

# Reconstruct route starting from city 1
route = [1]
current = 1
while True:
    next_city = None
    for j in cities:
        if current != j and value(x[(current,j)]) > 0.5:
            next_city = j
            break
    if next_city is None:
        break
    if next_city == 1:
        route.append(1)
        break
    route.append(next_city)
    current = next_city

print("\nRoute order:", " -> ".join(str(r) for r in route))
