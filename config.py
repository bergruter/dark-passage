class Config: # в будущем создать кнопку настроек
    """Главные параметры"""
    WIDTH = 1920
    HEIGHT = 1080
    TILE_SIZE = 40
    ROWS = HEIGHT // TILE_SIZE
    COLS = WIDTH // TILE_SIZE
    MONSTER_COUNT = 3

class Colors:
    """Используемые цвета"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)