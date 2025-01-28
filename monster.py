import pygame
import random
from config import Config, Colors

class Monster:
    """Создаем класс для управления монстрами"""
    def __init__(self, maze):
        """Инициализируем монстра"""
        while True:
            self.x = random.randint(2, Config.COLS - 3)
            self.y = random.randint(2, Config.ROWS - 3)
            if maze[self.y][self.x] == 0:
                break

    def draw(self, screen): # в будущем заменить на изображение
        """Создаем отображение монстра"""
        pygame.draw.rect(
            screen,
            Colors.RED,
            (
                self.x * Config.TILE_SIZE + 5,
                self.y * Config.TILE_SIZE + 5,
                Config.TILE_SIZE - 10,
                Config.TILE_SIZE - 10,
            ),
        )