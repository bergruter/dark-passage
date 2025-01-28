from config import Colors

class HUD: # в будущем добавить количество пройденных мини игр(?)
    """Класс для управления вывода дополнительного текста"""
    @staticmethod
    def draw(screen, font, monster_count):
        hud_text = font.render(
            f"Монстров осталось: {monster_count}", True, Colors.WHITE
        )
        screen.blit(hud_text, (10, 10))