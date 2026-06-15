try:
    # print(name)
    print(1 / 0)
except NameError as e:
    print("变量名不存在", e)
except ZeroDivisionError as e:
    print("0 不能作为被除数", e)
except TypeError as e:
    print("类型有误!", e)
except Exception as e:
    print("程序运行出错了!")
finally:
    print("资源释放")
