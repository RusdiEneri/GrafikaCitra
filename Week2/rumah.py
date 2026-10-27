import matplotlib.pyplot as plt
#segitiga atap
xs = [1, 4, 2.5, 1]
ys = [1, 1, 4, 1]
plt.fill(xs, ys, color='red', alpha=1)
plt.plot(xs, ys, "o-", color='black')
plt.axis('equal')

#jajar genjang atap
xs = [4, 2.5, 7, 7, 8.5]
ys = [1, 4, 4, 4, 1]
plt.fill(xs, ys, color='red', alpha=1)
plt.plot(xs, ys, "o-", color='black')
plt.axis('equal')

#tembokdepan
xs = [1, 1, 4, 4, 4]
ys = [1, -2, -2, 1, 1]
plt.fill(xs, ys, color='green', alpha=0.35)
plt.plot(xs, ys, "o-", color='black')
plt.axis('equal')

#pintu dan 2 jendela
#pintu
xs = [2, 2, 3, 3, 2]
ys = [-0.5, -2, -2, -0.5, -0.5]
plt.fill(xs, ys, color='brown', alpha=0.35)
plt.plot(xs, ys, color='black')
plt.axis('equal')

#jendela1
xs = [1.2, 1.2, 1.8, 1.8, 1.2]
ys = [0, -1, -1, 0, 0]
plt.fill(xs, ys, color='white', alpha=0.35)
plt.plot(xs, ys, color='black')
plt.axis('equal')

#jendela2
xs = [3.2, 3.2, 3.8, 3.8, 3.2]
ys = [0, -1, -1, 0, 0]
plt.fill(xs, ys, color='white', alpha=0.35)
plt.plot(xs, ys, color='black')
plt.axis('equal')

#temboksamping
xs = [4, 4, 8.5, 8.5, 4]
ys = [1, -2, -2, 1, 1]
plt.fill(xs, ys, color='green', alpha=0.35)
plt.plot(xs, ys, "o-", color='black')
plt.axis('equal')

#jendelasamping 1
xs = [4.4, 4.4, 5.6, 5.6, 4.4]
ys = [0.5, 0.2, 0.2, 0.5, 0.5]
plt.fill(xs, ys, color='white', alpha=0.35)
plt.plot(xs, ys, color='black')
plt.axis('equal')

#jendelasamping 2
xs = [6.4, 6.4, 7.6, 7.6, 6.4]
ys = [0.5, 0.2, 0.2, 0.5, 0.5]
plt.fill(xs, ys, color='white', alpha=0.35)
plt.plot(xs, ys, color='black')
plt.axis('equal')

plt.title("Gambar Rumah 2D")
# plt.grid(True)
plt.show()
