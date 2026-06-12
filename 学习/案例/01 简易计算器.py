num1=float(input('num1:'))
num2=float(input('num2:'))
op=input('输入运算符:')
match op:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case _:
        print("error")