import pygame
from config import Config
from game import Game

def main():
    """Главный исполнительный файл"""
    pygame.init()
    screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
    pygame.display.set_caption("Maze Game")
    font = pygame.font.Font(None, 36)

    game = Game()
    game.run(screen, font)

if __name__ == "__main__":
    main()
