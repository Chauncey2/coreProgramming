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
            self.__update()

    def __action(self):
        """
        处理各种矩形坐标移动
        :return:
        """
        self.game_map.move_down()

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

    def __update(self):
        """
        刷新页面
        :return:
        """
        pygame.display.update()


def start():
    game_window = GameWindow()
    game_window.run()


if __name__ == '__main__':
    start()
