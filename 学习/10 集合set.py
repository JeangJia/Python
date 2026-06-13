# 无序,不可重复,可修改
print("定义:")  # 定义
s1 = {"A", "B", "C", "A"}
s2 = set()  # 定义空集合
print(s1, s2, type(s1), type(s2))

print("add():")  # 添加元素
s1.add("J")
print(s1)

print("remove():")  # 移除指定元素
s1.remove("J")
print(s1)

print("pop():")  # 随机删除集合中的元素并返回
s1.pop()
print(s1)

print("clear():") # 清空集合
s1.clear()
print(s1)

print("difference():") # 求两个集合的差集
s1={"A", "B", "C", "D"}
s2={"D", "E", "F", "G"}
print(s1.difference(s2))
print(s2.difference(s1))

print("union():")  # 求两个集合的并集
print(s1.union(s2))
print(s2.union(s1))

print("intersection():")  # 求两个集合交集
print(s1.intersection(s2))
print(s2.intersection(s1))
