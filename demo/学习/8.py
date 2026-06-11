def greet(someone):
    print(f'Hello {someone}')
greet('jia')


def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My's name is {pet_name.title()}")
describe_pet('liu')                                      #如果不调用则实参=形参(为默认值)
describe_pet('zheng',animal_type='pig')         #更改默认值
describe_pet('xiang','jiao')         #最简调用所有形参(需要注意顺序)

#--------------------------------------------------------------------------------------------------------------

def get_formatted_name(first_name,last_name,middle_name=''):           #空引号要放到末尾!!!
    if middle_name:                                                    #理解为如果有
        full_name=f"{first_name}{middle_name}{last_name}"
    else:
        full_name=f"{first_name}{last_name}"
    return full_name.title()                                            #定义完后最后返回
outcome=get_formatted_name('jia','yi')
print(outcome)
outcome=get_formatted_name('jia','hang','yi')
print(outcome)

#--------------------------------------------------------------------------------------------------------------

show_message=[1,2,3,4,5]
def messages(show):
    for message in show:
        print(f"消息为{message}")
messages(show_message[-1:])                               #使用索引调用范围列表

#--------------------------------------------------------------------------------------------------------------

def make_pizza(*toppings):                                    #相当于创建了一个名为toppings的元组(两个**为字典)
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'{topping}')
make_pizza('fish')
make_pizza('cake','beef','milk')

def make_pizza(size,*toppings):
    print(f'\nMaking a {size}(m) pizza with the following toppings:')
    for topping in toppings:
        print(f'{topping}')
make_pizza(12,'fish')
make_pizza(18,'cake', 'beef', 'milk')


