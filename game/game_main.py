from game import game_map, hero_plane
import pygame
import sys

WINDOW_WIDTH = 512

WINDOW_HEIGHT = 768


class GameWindow(object):

    def __init__(self):
        # 实例化pygame
        pygame.init()
        # 创建游戏窗口
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0)
        # 添加游戏标题
        pygame.display.set_caption("飞机大战")
        # 设置窗口的图标icon
        image_icon = pygame.image.load("./res/images/app.ico")
        pygame.display.set_icon(image_icon)

        # 创建地图实例
        self.game_map = game_map.GameMap()
        # 创建玩家飞机
        self.hero_plane = hero_plane.HeroPlane()

    def run(self):

        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()

    def __action(self):
        """
        处理各种矩形坐标移动
        :return:
        """
        self.game_map.move_down()
        # 遍历子弹
        for bullet in self.hero_plane.bullet_list:
            if bullet.is_shot:
                bullet.move_up()

    def __draw(self):
        """
        根据矩形坐标对元素进行回测
        :return:
        """
        # 添加背景图片
        self.window.blit(self.game_map.img_1, (0, self.game_map.img1_y))
        self.window.blit(self.game_map.img_2, (0, self.game_map.img2_y))

        # 添加英雄飞机
        self.window.blit(self.hero_plane.img, (self.hero_plane.img_rect[0], self.hero_plane.img_rect[1]))

        # 添加子弹
        for bul in self.hero_plane.bullet_list:
            if bul.is_shot:
                self.window.blit(bul.bullet_img, (bul.bullet_img_rect[0], bul.bullet_img_rect[1]))

    def __event(self):
        """
        处理窗口的监听事件
        :return:
        """
        # 获取所有窗口的事件监听
        event_list = pygame.event.get()
        for event in event_list:
            # 鼠标单击关闭事件
            if event.type == pygame.QUIT:
                self.game_over()

            # 监听按下事件
            if event.type == pygame.KEYDOWN:
                # 是否按下的是Esc
                if event.key == pygame.K_ESCAPE:
                    self.game_over()
                # 是否按下的是空格
                if event.key == pygame.K_SPACE:
                    self.hero_plane.shoot()

        # 监听长按事件 -> 元组(0没按下，1长按了) 字母对应阿斯克码
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.hero_plane.move_up()

        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.hero_plane.move_down()

        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.hero_plane.move_left()

        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.hero_plane.move_right()

    def __update(self):
        """
        刷新页面
        :return:
        """
        pygame.display.update()

    def game_over(self):
        pygame.quit()
        sys.exit()


