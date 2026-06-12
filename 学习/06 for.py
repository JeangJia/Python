# for 元素 in 待处理数据集:
#     循环体
# else :
#     循环结束时,执行的代码

# range 生成数据集
# range(end) -> [0,end)
# range(begin,end) -> [begin,end)
# range(begin,end,step) -> [begin,begin+step,...,end)

msg = "Hello Python"
for i in msg:
    print(i)
total = 0
for i in range(100, 500):
    if not i % 3:
        total += i
print(total)
