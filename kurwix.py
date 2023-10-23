import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Kurwix')
clock = pygame.time.Clock()
terminal_font = pygame.font.Font('IF-game/Terminal.ttf', 16)

text_test = ''
add_this = 'Tekst jak terminal. Dodaj tekst, do ustawienia predkosci wyswietlania tekstu. Dlugiego tekstu.'
i = 0
print(len(add_this))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if i < len(add_this):
        text_test = text_test + add_this[i]
    text_surface = terminal_font.render(text_test, True, 'White')
    screen.blit(text_surface, (5, 10))
    i += 1

    pygame.display.update()
    clock.tick(40)  # Pętla while nie działa szybciej niż 60 razy na sekundę. Ogranicznik prędkości gry.
