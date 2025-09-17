import matplotlib.pyplot as plt
import networkx as nx

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# =====================
# 1. Graf Sederhana
# =====================
G1 = nx.Graph()
G1.add_edges_from([("1", "4"), ("1", "2"), ("4", "2"), ("4", "3"), ("2", "3")])
pos1 = {"1": (0.5, 1), "2": (1, 0.5), "3": (0.5, 0), "4": (0, 0.5)}
nx.draw(G1, pos1, with_labels=True, node_color="lightgray", node_size=700, ax=axes[0])
edge_labels1 = {("1","4"):"e1", ("1","2"):"e2", ("4","2"):"e3", ("4","3"):"e4", ("2","3"):"e5"}
nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels1, ax=axes[0])
axes[0].set_title("Graf Sederhana")

# =====================
# 2. Graf Ganda (Multigraph)
# =====================
G2 = nx.MultiGraph()
edges2 = [("1","4","e1"), ("1","2","e2"), ("1","2","e3"), ("4","2","e6"), ("4","3","e4"), ("2","3","e5")]
for u,v,k in edges2:
    G2.add_edge(u,v,key=k)

nx.draw(G2, pos1, with_labels=True, node_color="lightgray", node_size=700, ax=axes[1])

# Tambahkan label edge manual (tengah sisi)
for u,v,k in edges2:
    x1, y1 = pos1[u]
    x2, y2 = pos1[v]
    xm, ym = (x1+x2)/2, (y1+y2)/2
    axes[1].text(xm, ym, k, fontsize=10, color="brown")

axes[1].set_title("Graf Ganda")

# =====================
# 3. Graf Semu (Pseudograph)
# =====================
G3 = nx.MultiGraph()
edges3 = [("v1","v2","e1"), ("v1","v1","e2")]
for u,v,k in edges3:
    G3.add_edge(u,v,key=k)

pos3 = {"v1": (0, 0), "v2": (1, 0)}
nx.draw(G3, pos3, with_labels=True, node_color="black", node_size=700, font_color="white", ax=axes[2])

# Tambahkan label edge manual
axes[2].text(0.5, 0.05, "e1", fontsize=10, color="brown")  # edge v1-v2
axes[2].text(-0.15, 0.2, "e2", fontsize=10, color="brown") # loop v1

axes[2].set_title("Graf Semu")

plt.show()
