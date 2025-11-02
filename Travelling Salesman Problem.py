from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, LpStatus, value, PULP_CBC_CMD

# --- 1. Definisi kota ---
cities = ["A", "B", "C", "D"]
n = len(cities)

# --- 2. Model optimasi ---
model = LpProblem("TSP_Tanpa_Dictionary", LpMinimize)

# --- 3. Variabel biner x_ij (rute antar kota) ---
x_AB = LpVariable("x_AB", 0, 1, LpBinary)
x_AC = LpVariable("x_AC", 0, 1, LpBinary)
x_AD = LpVariable("x_AD", 0, 1, LpBinary)
x_BA = LpVariable("x_BA", 0, 1, LpBinary)
x_BC = LpVariable("x_BC", 0, 1, LpBinary)
x_BD = LpVariable("x_BD", 0, 1, LpBinary)
x_CA = LpVariable("x_CA", 0, 1, LpBinary)
x_CB = LpVariable("x_CB", 0, 1, LpBinary)
x_CD = LpVariable("x_CD", 0, 1, LpBinary)
x_DA = LpVariable("x_DA", 0, 1, LpBinary)
x_DB = LpVariable("x_DB", 0, 1, LpBinary)
x_DC = LpVariable("x_DC", 0, 1, LpBinary)

# --- 4. Variabel urutan kunjungan (MTZ) ---
uA = LpVariable("uA", 1, n)
uB = LpVariable("uB", 1, n)
uC = LpVariable("uC", 1, n)
uD = LpVariable("uD", 1, n)

# --- 5. Fungsi tujuan: langsung masukkan jarak antar kota ---
model += (
    10 * x_AB + 15 * x_AC + 20 * x_AD +
    10 * x_BA + 35 * x_BC + 25 * x_BD +
    15 * x_CA + 35 * x_CB + 30 * x_CD +
    20 * x_DA + 25 * x_DB + 30 * x_DC
), "Total_Distance"

# --- 6. Kendala derajat (masuk dan keluar 1 kali per kota) ---
# Kota A
model += x_AB + x_AC + x_AD == 1  # keluar dari A
model += x_BA + x_CA + x_DA == 1  # masuk ke A

# Kota B
model += x_BA + x_BC + x_BD == 1  # keluar dari B
model += x_AB + x_CB + x_DB == 1  # masuk ke B

# Kota C
model += x_CA + x_CB + x_CD == 1  # keluar dari C
model += x_AC + x_BC + x_DC == 1  # masuk ke C

# Kota D
model += x_DA + x_DB + x_DC == 1  # keluar dari D
model += x_AD + x_BD + x_CD == 1  # masuk ke D

# --- 7. MTZ subtour elimination ---
model += uA == 1  # A sebagai kota awal
for (ui, uj, xij) in [
    (uA, uB, x_AB), (uA, uC, x_AC), (uA, uD, x_AD),
    (uB, uA, x_BA), (uB, uC, x_BC), (uB, uD, x_BD),
    (uC, uA, x_CA), (uC, uB, x_CB), (uC, uD, x_CD),
    (uD, uA, x_DA), (uD, uB, x_DB), (uD, uC, x_DC),
]:
    model += ui - uj + n * xij <= n - 1

# --- 8. Selesaikan model ---
solver = PULP_CBC_CMD(msg=False)
model.solve(solver)

# --- 9. Tampilkan hasil ---
print("Status:", LpStatus[model.status])
print("Total jarak minimum:", value(model.objective))
print("\nRute yang diambil:")
for var in model.variables():
    if var.name.startswith("x_") and value(var) > 0.5:
        print(f"  {var.name} = 1")

print("\nNilai urutan (u):")
for u in [uA, uB, uC, uD]:
    print(f"  {u.name} = {value(u)}")
