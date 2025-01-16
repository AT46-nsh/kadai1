import matplotlib.pyplot as plt

# プロットするデータ
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# 散布図を描画
plt.scatter(x, y, color='blue', label='Data Points')

# 軸のラベルを追加
plt.xlabel('X軸 (X-axis)')
plt.ylabel('Y軸 (Y-axis)')

# グラフのタイトルを追加
plt.title('散布図 (Scatter Plot)')

# 凡例を表示
plt.legend()

# グラフを表示
plt.grid(True)
plt.show()
