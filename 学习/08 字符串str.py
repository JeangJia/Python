s="Hello-python"
print(s)
# s[0]='h' # 不可变性 不能进行修改
print("切片:")
print(s[6::])
print(s[-1:5:-1])

# find() 查找子串返回第一次出现的索引位置,没有返回-1
print("find():")
print(s.find("o"))
# count() 统计子串出现次数
print("count():")
print(s.count("o"))
# title() 首字母大写
print("title():")
print(s.title())
# upper() 所有字母大写
print("upper():")
print(s.upper())
# lower() 所有字母小写
print("lower():")
print(s.lower())
# split() 将字符串按指定字符切割到列表
print("split():")
print(s.split(" "))
# strip() 去除两端空格
print("strip():")
print(s.strip())
# replace 指定字串替换为新的内容
print("replace():")
print(s.replace("-","_"))
# startswith() / endswith() 判断字符串是否以指定字符串开头 / 结尾
print("startswith() / endswith():")
print(s.startswith("Hello"))
print(s.endswith("_"))
