import pygame

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class HeroPlane(object):
    def __init__(self):
        # 飞机图片
        self.img = pygame.image.load('res/images/hero2.png')
        # 英雄飞机的外框矩形 -> (x,y, 宽像素，高像素)
        self.img_rect = self.img.get_rect()
        # 飞机的初始位置
        self.img_rect.move_ip((WINDOW_WIDTH - self.img_rect[2]) / 2, (WINDOW_HEIGHT - self.img_rect[3]) - 50)
        # 飞机的移动速度
        self.speed = 3

        # 子弹弹夹

        def move_up(self):
            pass

        def move_down(self):
            pass

        def move_left(self):
            pass

        def move_right(self):
            pass

        def shoot(self):
            pass
