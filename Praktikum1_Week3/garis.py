import matplotlib.pyplot as plt
#garis
xs = [1, 4]
ys = [1, 1]
plt.fill(xs, ys, color='red', alpha=1)
plt.plot(xs, ys, "o-", color='black')
plt.axis('equal')

plt.title("Gambar Garis")
# plt.grid(True)
plt.show()
