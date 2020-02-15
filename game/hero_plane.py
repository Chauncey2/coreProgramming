import pygame
from game import bullet

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
        self.bullet_list = [bullet.Bullet() for _ in range(6)]

    def move_up(self):
        # 边界检查
        if self.img_rect[1] >= 0:
            self.img_rect.move_ip(0, -self.speed)  # move_ip(x.y)

    def move_down(self):
        # 边界检查
        if self.img_rect[1] <= WINDOW_HEIGHT - self.img_rect[3]:
            self.img_rect.move_ip(0, self.speed)  # move_ip(x.y)

    def move_left(self):
        # 边界检查
        if self.img_rect[0] >= 0:
            self.img_rect.move_ip(-self.speed, 0)  # move_ip(x.y)

    def move_right(self):
        # 边界检查
        if self.img_rect[0] <= WINDOW_WIDTH - self.img_rect[2]:
            self.img_rect.move_ip(self.speed, 0)  # move_ip(x.y)

    def shoot(self):
        # 遍历所有子弹
        for bul in self.bullet_list:
            if not bul.is_shot:
                # 设置子弹发射位置
                bul.bullet_img_rect[0] = self.img_rect[0] + (self.img_rect[2] - bul.bullet_img_rect[2]) / 2
                bul.bullet_img_rect[1] = self.img_rect[1] - (bul.bullet_img_rect[3] - 10)
                # 更新子弹状态
                bul.is_shot = True
                # 一次只能发射一颗子弹
                break
