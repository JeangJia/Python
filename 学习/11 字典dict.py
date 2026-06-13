# 字典 -> key : value -> 不能重复否则会被覆盖,key必须得是不可变的类型(str,int,float,tuple)
# 定义
dict1 = {
    "Jeang": 18,
    "Liu": 19,
}
print(dict1)
print("修改/添加:")
dict1["Jia"] = 20
print(dict1)

print("删除:")
dict1.pop("Jia") # 删除指定的key并返回对应的value
del dict1["Liu"] # 删除指定的key
print(dict1)

print("查询:")
print(dict1.get("Jia","nonentity")) # 查找指定key,未找到可添加提示信息不然会报错
print(dict1.keys()) # 获取所有key
print(dict1.values()) # 获取所有value
print(dict1.items()) # 获得所有键值对

print("遍历:")
for item in dict1.items(): # item 为元组
    print(item)