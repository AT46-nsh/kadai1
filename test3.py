import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

plt.scatter(x, y, color='blue', label='Data Points')

plt.xlabel('X軸 (X-axis)')
plt.ylabel('Y軸 (Y-axis)')

plt.title('散布図 (Scatter Plot)')

plt.legend()

plt.grid(True)
plt.show()
