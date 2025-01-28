import pygame
from config import Config, Colors

class Player:
    """Создаем класс для управления игроком"""
    def __init__(self, start_x=1, start_y=1):
        """Инициализируем игрока в стартовой позиции"""
        self.x = start_x
        self.y = start_y

    def move(self, dx, dy, maze):
        """Управление перемещением"""
        if maze[self.y + dy][self.x + dx] == 0:
            self.x += dx
            self.y += dy

    def draw(self, screen):
        """Рисуем игрока"""
        pygame.draw.rect(
            screen,
            Colors.GREEN,
            (
                self.x * Config.TILE_SIZE + 5,
                self.y * Config.TILE_SIZE + 5,
                Config.TILE_SIZE - 10,
                Config.TILE_SIZE - 10,
            ),
        )