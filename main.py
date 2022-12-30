import pygame
import sys
import pymysql
from pygame.locals import *


class BackMusicService(object):
    def __init__(self):
        pygame.init()
        # 设置音乐文件路径
        music_path = "source/music/bg_music.mp3"
        # 加载音乐文件
        pygame.mixer.music.load(music_path)
        # 设置循环播放
        pygame.mixer.music.play(-1)


class BackgroundService(object):
    def __init__(self):
        """初始化游戏界面宽度和高度"""
        self.screen_width = 160
        self.screen_height = 90
        self.size = self.screen_width, self.screen_height

    def draw_background(self):
        """画背景图"""
        pygame.init()
        size = self.size
        screen = pygame.display.set_mode(size)  # 屏幕尺寸
        img_path = "source/images/start_background.jfif"  # 背景图片
        img_surface = pygame.image.load(img_path).convert()
        img_surface = pygame.transform.scale(img_surface, size)
        pygame.display.set_caption('YGO!DualLinks')

        # 安装字体
        pygame.font.init()
        # 获取中文字体
        font_path = "source/font/start_game.TTF"
        cn_font = pygame.font.Font(font_path, 48)
        # 设置按钮的尺寸为屏幕宽度的1/10
        button_width = self.screen_width // 10
        button_height = button_width // 2
        # 使用中文字体创建按钮
        button_start = cn_font.render("开始", True, (11, 27, 63))
        button_start = pygame.transform.scale(button_start, (button_width, button_height))
        button_setting = cn_font.render("设置", True, (11, 27, 63))
        button_setting = pygame.transform.scale(button_setting, (button_width, button_height))
        button_exit = cn_font.render("退出", True, (11, 27, 63))
        button_exit = pygame.transform.scale(button_exit, (button_width, button_height))

        # 获取按钮的矩形边界
        button_start_rect = button_start.get_rect()
        button_setting_rect = button_setting.get_rect()
        button_exit_rect = button_exit.get_rect()
        # 设置按钮的位置为屏幕中央
        button_start_rect.center = (self.screen_width // 2, self.screen_height // 2)
        button_setting_rect.center = (self.screen_width // 2, self.screen_height // 2 + button_height + 10)
        button_exit_rect.center = (self.screen_width // 2, self.screen_height // 2 + 2 * (button_height + 10))

        return screen, img_surface, button_start, button_start_rect, button_setting, button_setting_rect, button_exit, button_exit_rect


def main():
    background_service = BackgroundService()
    BackMusicService()  # 背景音乐
    screen, img_surface, button_start, button_start_rect, button_setting, button_setting_rect, button_exit, button_exit_rect = background_service.draw_background()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            # 处理鼠标事件
            elif event.type == MOUSEBUTTONDOWN:
                # 只有在左键点击时才触发点击事件
                if event.button == 1:
                    # 获取鼠标坐标
                    x, y = pygame.mouse.get_pos()
                    # 判断是否点击了按钮
                    if button_start_rect.collidepoint(x, y):
                        # 点击了开始游戏按钮
                        print('开始游戏')
                    elif button_setting_rect.collidepoint(x, y):
                        # 点击了设置按钮
                        print('设置')
                    elif button_exit_rect.collidepoint(x, y):
                        # 点击了退出按钮
                        print('退出')
                        sys.exit()

        # 绘制背景图片
        screen.blit(img_surface, (0, 0))
        # 绘制 "开始游戏" 按钮
        screen.blit(button_start, button_start_rect)
        # 绘制 "设置" 按钮
        screen.blit(button_setting, button_setting_rect)
        # 绘制 "退出" 按钮
        screen.blit(button_exit, button_exit_rect)
        pygame.display.update()


if __name__ == '__main__':
    main()
