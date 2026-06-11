names=['小明','小张','小红']
for name  in names:
    print(f"\n{name}你好!")
    print('今天还好吧')


for n in range(3):        #range()可以生成一系列数
    print(n)
print(list(range(3)))     #使用list)函数可以将range()的结果直接转化为表格
print(list(range(10)))

for y in range(1,10,2):
    print(y)

z=[]
for x in range(1,11):
    z.append(x**3)
print(z)


names=['小明','小红','小花','小李']
print('你的朋友有:')
for name in names[:3]:              #[:]可以剪切列表也可以用于作为被复制的列表 如:name=names[:](不包含尾数!!!)
    print(name)


Foods = ('A','B','C','D','E')       #元组_不可改数据
for Food in Foods:
    print(Food)
