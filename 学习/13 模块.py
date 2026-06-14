import demo_module
from demo_module import say_hi
from demo_module import PI as PI

# import demo_module (as 别名)
# from demo_module import say_hi (as 别名)

# 导入 __all__ 里面的内容
# from demo_module import *

say_hi("Jeang")
demo_module.outline(50)
print(PI)
