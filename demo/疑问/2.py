a = 23
flag=False
for i in range(2,a):
    if a % i == 0:
        flag=True

if flag:
    print('是素数')
else:
    print('是合数')