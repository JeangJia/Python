import numpy as np
import pandas as pd

# 2
arr = np.arange(2, 14).reshape(3, 4)
print(arr[0:2, 1:4])
print(arr)
# axis=0 表示按列求和，axis=1 表示按行求和
print(arr.sum(axis=0).tolist())
print(arr.sum(axis=1).tolist())

# 3
df = pd.DataFrame(
    {
        "name": ["商品A", "商品B", "商品C", "商品D"],
        "sales": [32, 56, 41, 68]
    },
)
sel = df.loc[df["sales"] > 40]
sel = sel.sort_values("sales", ascending=False)
print(sel["name"].tolist())

# 4
import matplotlib.pyplot as plt

x = ["1月", "2月", "3月", "4月"]
y = [42, 55, 48, 63]
plt.plot(x, y, marker="o")  # 折线图，marker="o" 为圆形标记
plt.title("社团月度参与人数")  # 标题
plt.xlabel("月份")  # x 轴标签
plt.ylabel("人数")  # y 轴标签
plt.show()  # 显示图表
