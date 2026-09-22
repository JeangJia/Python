print('哈喽呀!我是一个消息收集器 &>_<& ')
dictionary = {}
users_input = True
while users_input :
   names=input('你的名字是?')
   message=input('请输入您想输入的消息:')
   dictionary[names]=message
   repeat=input('是否还有谁想输入消息?(yes/no)')
   if repeat =='no':
      users_input = False
print('-------所有结果如下:------')
for name,message in dictionary.items():
   print(f"{name}输入的消息为:{message}")
