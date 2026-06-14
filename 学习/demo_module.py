# __all__ 指定 from ... import * 导入的内容默认全部
__all__ = ["say_hi", "PI"]

PI = 3.1415926


def say_hi(name=""):
    print(f"Hello {name}")


def outline(l=10):
    print("-" * l)


# __name__ 内置变量,表示当前模块名(直接运行值为:__main__,当该模块被导入时值为模块名)
# print(__name__)
# 可以用与在当前模块检查代码
if __name__ == '__main__':
    say_hi()
    outline()
