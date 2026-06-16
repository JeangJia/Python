# 导入 pygame 库（做游戏用）和 sys 库（退出程序用）
import pygame
import sys

# 初始化 pygame 的所有模块，必须先写这句
pygame.init()

# 创建游戏窗口，参数是 (宽度, 高度)
screen = pygame.display.set_mode((800, 600))
# 设置窗口标题
pygame.display.set_caption("带注释的 Pygame 小案例")

# 定义颜色，格式是 (红, 绿, 蓝)，取值 0~255
WHITE = (255, 255, 255)  # 白色
RED   = (255, 0, 0)      # 红色

# 方块的初始坐标（屏幕正中间）
x = 400
y = 300

# 方块移动速度
speed = .5

# 游戏主循环：游戏一直运行，直到关闭窗口
while True:
    # ============= 1. 事件处理 =============
    # 获取所有发生的事件（鼠标点击、按键、关闭窗口等）
    for event in pygame.event.get():
        # 如果点了窗口右上角的关闭按钮
        if event.type == pygame.QUIT:
            pygame.quit()  # 关闭 pygame
            sys.exit()      # 退出程序

    # ============= 2. 键盘控制移动 =============
    # 获取当前所有被按下的键
    keys = pygame.key.get_pressed()

    # 根据方向键修改 x、y 坐标
    if keys[pygame.K_LEFT]:
        x -= speed  # 左移：x 减小
    if keys[pygame.K_RIGHT]:
        x += speed  # 右移：x 增大
    if keys[pygame.K_UP]:
        y -= speed  # 上移：y 减小
    if keys[pygame.K_DOWN]:
        y += speed  # 下移：y 增大

    # ============= 3. 绘制画面 =============
    screen.fill(WHITE)  # 用白色填充整个屏幕（清屏）

    # 画一个矩形
    # 参数：窗口, 颜色, (左上角x, 左上角y, 宽度, 高度)
    pygame.draw.rect(screen, RED, (x, y, 50, 50))

    # ============= 4. 更新屏幕显示 =============
    pygame.display.flip()  # 把画好的内容刷新到屏幕上