import matplotlib.pyplot as plt

bunder = plt.Circle((2,2), 1, fill = False, edgecolor='black', linewidth=1)

ax = plt.subplot()
ax.add_patch(bunder)

plt.axis('equal')
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.grid(True)
plt.title("Gambar Lingkaran")
plt.show()