import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


def test_func(x, offset=5):
    return x * 2 - offset


# 1
print(test_func(12))
res = list(map(lambda x: x // 2, [6, 11, 15]))
print(res)

# 2
arr = np.arange(2, 18).reshape(4, 4)
sub = arr[1:3, 1:3]
print(sub.tolist())
print(arr.sum(axis=1).tolist())

# 3
df = pd.DataFrame({
    "video": ["v1", "v2", "v3", "v4"],
    "play": [2300, 890, 4100, 1600]
})
sel = df.loc[df["play"] > 2000].sort_values("play", ascending=True)
print(sel["video"].tolist())
print(sel["play"].sum())

# 4
time = [0, 1, 2, 3, 4]
temp = [22.1, 24.3, 25.0, 23.8, 22.6]
fig, ax = plt.subplots()
line, = ax.plot(time, temp, marker='D')
ax.set_title("Room Temperature")
ax.set_xlabel("hour")
print(line.get_ydata().tolist())
print(ax.get_title())
plt.close(fig)

# 6
df = pd.DataFrame({"name": ["A", "B", "C"], "score": [75, 88, 92]})
print(df)
res = df.loc[df["score"] >= 80]
print(res)

# 四
# 1
df = pd.DataFrame({
    "day": ["周一", "周二", "周三", "周四", "周五"],
    "launch": [1200, 1350, 1100, 1420, 1280],
    "dinner": [890, 950, 820, 1010, 970]
})
# 筛选午餐营收大于1200的记录
df_sel = df.loc[df["launch"] > 1200]
# 按午餐营收升序排序
df_sort = df_sel.sort_values("launch", ascending=True)
# 绘制柱状图，x为日期，y为午餐营收
plt.bar(df_sort["day"], df_sort["launch"])
# 设置标题
plt.title("食堂午餐营收统计")
# 设置y轴标签
plt.ylabel("营收(元)")
# 显示图表
plt.show()
