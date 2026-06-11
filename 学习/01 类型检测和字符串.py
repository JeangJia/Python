# type() 检测数据类型
# isinstance(数据,类型) 判断类型 返回 bool
num = 99
print(type(num), isinstance(num, int))

# 字符串格式化
s = "Hello"
print("%s World %d" % (s, num))
print(f"{s} World {num}")
