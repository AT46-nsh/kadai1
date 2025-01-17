import random
import matplotlib.pyplot as plt

x = [random.random() for _ in range(50)]
y = [random.random() for _ in range(50)]

plt.scatter(x, y, color='blue')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()
