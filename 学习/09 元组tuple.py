t1 = (12, 45, 32, 12,)
t2 = (12,)
t3 = 12, 45, 32, 12, # 组包
print(t1, t2, t3)
# 元组不可以进行修改
print(t1, type(t1))
# count()
print(t1.count(12))
# index()
print(t1.index(12))
# 解包
print("解包:")
a, b, c, d = t1
print(a, b, c, d)
x, *y, z = t1
print(x, y, z)
