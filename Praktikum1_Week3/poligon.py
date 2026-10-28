import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, RegularPolygon

# Fungsi segitiga siku-siku
def segitiga(ax):
    titik = [(1, 1), (3, 1), (1, 3)]
    bangun = Polygon(titik, fill=False, edgecolor='black')
    ax.add_patch(bangun)
    ax.set_title("Segitiga Siku-Siku")


# Fungsi segi tujuh
def segi_tujuh(ax):
    bangun = RegularPolygon((2, 2), numVertices=7, radius=1.5,
                            fill=False, edgecolor='black')
    ax.add_patch(bangun)
    ax.set_title("Segi Tujuh")


# Fungsi segi lima
def segi_lima(ax):
    bangun = RegularPolygon((2, 2), numVertices=5, radius=1.5,
                            fill=False, edgecolor='black')
    ax.add_patch(bangun)
    ax.set_title("Segi Lima")


# Membuat satu figure dengan 3 subplot
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Memanggil masing-masing fungsi
segitiga(axs[0])
segi_tujuh(axs[1])
segi_lima(axs[2])

# Pengaturan semua subplot
for ax in axs:
    ax.set_aspect('equal')
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()