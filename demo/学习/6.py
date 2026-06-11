alien_0={'color':'green',}
print(alien_0['color'])      #访问字典中的值与访问列表类似

alien_0['points']='5'        #添加键值对
alien_0['x_position']=0      #数字可以不用引号
print(alien_0)

alien_0['color']='yellow'    #修改字典中的值和添加类似
print(alien_0)

del alien_0['points']        #删除键值对(注意与列表中的del区别)
print(alien_0)

favorite_languages={          #数量多时可以竖条更加清晰
    'jen': 'python',
    'sarah' : 'c',
    'edward':'rust',
    'phil':'python',
    }
print(favorite_languages)
language=favorite_languages['sarah'].title()        #数量多时使用变量可以更好的找到想要的值
print(f"Sarah's favorite language is {language}")

names=favorite_languages.get('JIA','not have')      #使用get（）来检验字典里是非有该值，没有将打印后面编写的消息
print(names)

for key,value in favorite_languages.items():        #使用两个变量和items（）结合for循环来遍历字典
    print(f"\nkey:{key}")
    print(f"value:{value}")
    print(f"{key}:{value.title()}\n")

for name in favorite_languages.keys():              #keys()遍历字典所有的键(在遍历字典使会默认遍历所有的键 也就是说可以忽略 'keys（）'）
    print(name.title())
for  language in favorite_languages.values():       #values()遍历字典所有的值
    print(language.title())
for name in sorted(favorite_languages.keys()):      #sorted()可以让所有键按字母排序
    print(f"{name.upper()}")
for language in set(favorite_languages.values()):   #set（）用于剔除重复项
    print(language.title())

#-------------------------------------------------------------------------------------------------------------------------------------------

favorite_languages = {                              #字典储存列表
        'jen':[ 'python','java'],
        'sarah': 'c',
        'edward': ['rust'],
        'phil': ['python','c'],
        }
print(favorite_languages)
for name,languages in favorite_languages.items():
    print(f"\n {name.title()}'s "
          f"favorite languages are:")               #字典中存在多个值使使用两个for循环来遍历键值
    for language in languages :
        print(f"\t{language.title()}")

