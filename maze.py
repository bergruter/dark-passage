import pygame
import random
from config import Config, Colors


class Maze:
    """Класс для управления генерацией лабиринта"""
    def __init__(self):
        """Инициализируем пустой лабиринт"""
        self.maze = None
        self.surface = None

    def generate(self):
        """Создаем генерацию лабиринта"""
        maze = [[1] * Config.COLS for _ in range(Config.ROWS)]

        def carve_passages(cx, cy):
            """Создаем проходы в лабиринте"""
            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = cx + dx * 2, cy + dy * 2
                if (
                    0 < ny < Config.ROWS - 1 and
                    0 < nx < Config.COLS - 1 and
                    maze[ny][nx] == 1
                ):
                    maze[cy + dy][cx + dx] = 0
                    maze[ny][nx] = 0
                    carve_passages(nx, ny)

        maze[1][1] = 0
        carve_passages(1, 1)
        maze[Config.ROWS - 2][Config.COLS - 2] = 0

        self.maze = maze
        self._draw_to_surface()

    def _draw_to_surface(self):
        """Создаем отрисовку лабиринта"""
        self.surface = pygame.Surface((Config.WIDTH, Config.HEIGHT))
        for y in range(Config.ROWS):
            for x in range(Config.COLS):
                color = Colors.WHITE if self.maze[y][x] == 0 else Colors.BLACK
                pygame.draw.rect(
                    self.surface,
                    color,
                    (x * Config.TILE_SIZE, y * Config.TILE_SIZE, Config.TILE_SIZE, Config.TILE_SIZE),
                )

    def draw(self, screen):
        """Рисуем лабиринт"""
        if self.surface:
            screen.blit(self.surface, (0, 0))