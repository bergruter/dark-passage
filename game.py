import pygame
import sys
from config import Config, Colors
from maze import Maze
from player import Player
from monster import Monster
from hud import HUD
from minigames import MiniGames

class Game:
    """Класс для управления игрой"""
    def __init__(self):
        """Инициализируем игру"""
        self.maze = Maze()
        self.player = Player()
        self.monsters = []
        self.exit_point = (Config.COLS - 2, Config.ROWS - 2)
        self.image = pygame.image.load('images/start_screen.jpeg')

    def start_screen(self, screen, font):
        """Создаем стартовый экран и необходимые кнопки"""
        while True:
            # Создаем черный экран с кнопками
            # screen.fill(Colors.BLACK)
            screen.blit(self.image, (0, 0))
            title_text = font.render("Maze Game", True, Colors.WHITE)
            new_game_text = font.render("Новая игра (N)", True, Colors.WHITE)
            exit_text = font.render("Выход (Q)", True, Colors.WHITE)

            # Задаем положение названию игры
            screen.blit(
                title_text,
                (Config.WIDTH // 2 - title_text.get_width() // 2, Config.HEIGHT // 4),
            )
            # Задаем положение для Новой игры
            screen.blit(
                new_game_text,
                (Config.WIDTH // 2 - new_game_text.get_width() // 2, Config.HEIGHT // 2),
            )
            # Задаем положение для Выхода
            screen.blit(
                exit_text,
                (Config.WIDTH // 2 - exit_text.get_width() // 2, Config.HEIGHT // 2 + 50),
            )

            pygame.display.flip()

            # Проверяем нажатие клавиш
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        return True
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def initialize_game(self):
        """Инициализируем генерацию лабиринта, игрока и монстров"""
        self.maze.generate()
        self.player = Player()
        self.monsters = [Monster(self.maze.maze) for _ in range(Config.MONSTER_COUNT)]

    def handle_collisions(self):
        """Проверяем столкновение с монстром и конечной точкой"""
        for monster in self.monsters:
            if self.player.x == monster.x and self.player.y == monster.y:
                return "monster"

        if (self.player.x, self.player.y) == self.exit_point:
            return "exit"

        return None

    def run(self, screen, font):
        """Запускаем игру"""
        if not self.start_screen(screen, font):
            return

        self.initialize_game()

        while True:
            screen.fill(Colors.BLACK)
            self.maze.draw(screen)

            # рисуем начальную точку
            pygame.draw.rect(
                screen,
                Colors.BLUE,
                (
                    Config.TILE_SIZE + Config.TILE_SIZE // 4,
                    Config.TILE_SIZE + Config.TILE_SIZE // 4,
                    Config.TILE_SIZE // 2,
                    Config.TILE_SIZE // 2,
                ),
            )

            # рисуем игрока
            pygame.draw.rect(
                screen,
                Colors.GREEN,
                (
                    (Config.COLS - 2) * Config.TILE_SIZE + Config.TILE_SIZE // 4,
                    (Config.ROWS - 2) * Config.TILE_SIZE + Config.TILE_SIZE // 4,
                    Config.TILE_SIZE // 2,
                    Config.TILE_SIZE // 2,
                ),
            )

            self.player.draw(screen)
            for monster in self.monsters:
                monster.draw(screen)

            HUD.draw(screen, font, len(self.monsters))

            # проверка столкновений с монстром
            collision_result = self.handle_collisions()
            if collision_result == "monster":
                success = MiniGames.play_random(screen, font)
                if not success:
                    self.show_message(
                        screen, font, "Вы проиграли в мини-игре. Попробуйте снова."
                    )
                    if not self.start_screen(screen, font):
                        pygame.quit()
                        sys.exit()
                    self.initialize_game()
                else:
                    self.monsters.pop(0)

            # Проверка достижения выхода
            elif collision_result == "exit":
                self.show_message(
                    screen, font, "Поздравляем! Вы прошли лабиринт!"
                )
                if not self.start_screen(screen, font):
                    pygame.quit()
                    sys.exit()
                self.initialize_game()

            # выход из игры закрытием окна
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # проверка нажатий клавиш во время игры
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_LEFT]:
                self.player.move(-1, 0, self.maze.maze)
            if keys[pygame.K_RIGHT]:
                self.player.move(1, 0, self.maze.maze)
            if keys[pygame.K_UP]:
                self.player.move(0, -1, self.maze.maze)
            if keys[pygame.K_DOWN]:
                self.player.move(0, 1, self.maze.maze)

            pygame.display.flip()

    def show_message(self, screen, font, message):
        """Создаем вывод сообщений"""
        screen.fill(Colors.BLACK)
        message_text = font.render(message, True, Colors.WHITE)
        screen.blit(
            message_text,
            (Config.WIDTH // 2 - message_text.get_width() // 2, Config.HEIGHT // 2),
        )
        pygame.display.flip()
        pygame.time.wait(2000)