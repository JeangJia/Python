num1=float(input('num1:'))
num2=float(input('num2:'))
op=input('输入运算符:')
match op:
    case '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    case '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    case '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    case '/' if num2:
        print(f"{num1} / {num2} = {(num1 / num2):.1f}")
    case _:
        print("error")