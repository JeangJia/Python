# import demo_utils.demo_fun
# from demo_utils import demo_fun
# from demo_utils.demo_fun import say_hi

# 必须在 __init__ 定义 __all__ 才可以用 * 导入
from demo_utils import *

demo_fun.say_hi("jia")
