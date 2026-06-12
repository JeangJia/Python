# 定义
s = [11,11,33,22,"A","Jeang","Jia",True]
print(s)
print(type(s))
print("访问:") # 访问
print(s[0],s[-1])

print("追加:") # 追加
s.append("false") # 末尾追加
s.insert(0,"true") # 指定位置插入
print(s)

print("删除:") # 删除
del s[-1] # 指定索引删除
s.pop() # 删除末尾
s.pop(0) # 指定索引删除
s.remove(11) # 删除第一个指定的数据
print(s)

print("修改:") # 修改
s[3]="ABC"
print(s)

print("遍历:") # 遍历
for item in s:
    print(item,end=",")
print('')

print("切片:") # 切片
# s[start:end:step]
# 不指定(start 默认0,end 默认列表长度,step 默认1)
print(s[0:3:1])

print("排序") # 排序
t=s[:3]
t.sort()
print(t)

print("反转:") # 反转
t.reverse()
print(t)

print("其它:") # 其它
print(f"len={len(t)}")
print(f"min={min(t)}")
print(f"max={max(t)}")
print(f"sum={sum(t)}")

