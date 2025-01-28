import pygame
import random
import sys
from config import Colors, Config

class MiniGames:
    """Класс для управления мини-играми"""
    @staticmethod
    def hangman(screen, font):
        """Создаем игру Виселица"""
        words = ["привет", "привет", "привет", "привет"]
        word_to_guess = random.choice(words)
        guessed_word = ["_"] * len(word_to_guess)
        attempts_left = 6

        while attempts_left > 0 and "_" in guessed_word:
            screen.fill(Colors.BLACK)

            attempts_text = font.render(
                f"Осталось попыток: {attempts_left}", True, Colors.WHITE
            )
            word_text = font.render(" ".join(guessed_word), True, Colors.WHITE)
            input_text = font.render("Введите букву: ", True, Colors.WHITE)

            screen.blit(
                attempts_text,
                (Config.WIDTH // 2 - attempts_text.get_width() // 2, Config.HEIGHT // 4),
            )
            screen.blit(
                word_text,
                (Config.WIDTH // 2 - word_text.get_width() // 2, Config.HEIGHT // 2),
            )
            screen.blit(
                input_text,
                (
                    Config.WIDTH // 2 - input_text.get_width() // 2,
                    Config.HEIGHT // 4 + attempts_text.get_height() + 10,
                ),
            )

            pygame.display.flip()

            guess = ""
            while len(guess) != 1 or not guess.isalpha():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return False
                        elif event.unicode.isalpha() and len(event.unicode) == 1:
                            guess = event.unicode.lower()

            if guess in word_to_guess:
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        guessed_word[i] = guess
            else:
                attempts_left -= 1

        return "_" not in guessed_word

    @staticmethod
    def play_random(screen, font): # в будущем нужно расширить количество игр
        """Создаем выбор мини-игр"""
        return MiniGames.hangman(screen, font)