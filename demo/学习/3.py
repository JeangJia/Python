shop=['茶π','hello','水']
#可获取列表元素
print(shop[1].title())
#3.1
name=['贾','羿','航']
print(name[0])
print(name[1])
print(name[2])
#3.2
print('hello  ' +name[0])
#3.3
vehicle=['bus','car','bickcle']
print(vehicle)
print('每天坐'+vehicle[0]+'上学')
#(组)[](修改列表)
vehicle[0]='che'
print(vehicle)#
# .append()(追加元素)
vehicle.append('hh')
print(vehicle)
print(f"{name}{vehicle}")
# del(删除位置元素)
del name[0]
print(name)
# pop()(剪切最后或任意元素)
names=name.pop()
print(names)
print(name)
#remove()(删除列表中特定的元素)
vehicle.remove('che')
print(vehicle)
print(len(name))

Ebglish=['A','E','C','F']
Ebglish.sort()
print(Ebglish)
Ebglish.sort(reverse=True)  #直接使用reverse可以反向列表_English.reverse()
print(Ebglish)
print(sorted(Ebglish))
print(Ebglish)
print(len(Ebglish))
print(Ebglish[-1])