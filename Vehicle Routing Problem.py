import pulp

# Membuat model
model = pulp.LpProblem("VRP_Distribusi_Gas", pulp.LpMinimize)

# Variabel biner x_ij
x_01 = pulp.LpVariable('x_01', cat='Binary')
x_02 = pulp.LpVariable('x_02', cat='Binary')
x_03 = pulp.LpVariable('x_03', cat='Binary')
x_10 = pulp.LpVariable('x_10', cat='Binary')
x_12 = pulp.LpVariable('x_12', cat='Binary')
x_13 = pulp.LpVariable('x_13', cat='Binary')
x_20 = pulp.LpVariable('x_20', cat='Binary')
x_21 = pulp.LpVariable('x_21', cat='Binary')
x_23 = pulp.LpVariable('x_23', cat='Binary')
x_30 = pulp.LpVariable('x_30', cat='Binary')
x_31 = pulp.LpVariable('x_31', cat='Binary')
x_32 = pulp.LpVariable('x_32', cat='Binary')

# Variabel MTZ untuk kapasitas
Q = 15
u1 = pulp.LpVariable('u1', lowBound=8, upBound=15)
u2 = pulp.LpVariable('u2', lowBound=9, upBound=15)
u3 = pulp.LpVariable('u3', lowBound=5, upBound=15)

# -----------------------------------
# Fungsi tujuan: minimisasi total jarak
# -----------------------------------
model += (
    4*x_01 + 6*x_02 + 3*x_03 +
    4*x_10 + 2*x_12 + 5*x_13 +
    6*x_20 + 2*x_21 + 3*x_23 +
    3*x_30 + 5*x_31 + 3*x_32
)

# Kendala kunjungan setiap toko
model += x_10 + x_12 + x_13 == 1
model += x_20 + x_21 + x_23 == 1
model += x_30 + x_31 + x_32 == 1

model += x_01 + x_21 + x_31 == 1
model += x_02 + x_12 + x_32 == 1
model += x_03 + x_13 + x_23 == 1

# Kendaraan dari dan ke depot (2 kendaraan)
model += x_01 + x_02 + x_03 == 2
model += x_10 + x_20 + x_30 == 2

# MTZ kapasitas (mencegah subtour)
model += u1 - u2 + Q*x_12 <= Q - 9
model += u1 - u3 + Q*x_13 <= Q - 5
model += u2 - u1 + Q*x_21 <= Q - 8
model += u2 - u3 + Q*x_23 <= Q - 5
model += u3 - u1 + Q*x_31 <= Q - 8
model += u3 - u2 + Q*x_32 <= Q - 9

# Selesaikan model
solver = pulp.PULP_CBC_CMD(msg=False)
model.solve(solver)

# Hasil
print("Status:", pulp.LpStatus[model.status])
print("Total jarak minimum =", pulp.value(model.objective))

# Tampilkan hasil variabel aktif
for v in model.variables():
    if pulp.value(v) > 0.5:
        print(v.name, "=", 1)
