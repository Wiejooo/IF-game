import pygame
from sys import exit

"""
Istalowanie poprzez PyIstallera
pyinstaller kurwix.py --onefile --windowed
w terminalu w folderze z grą. Potem przenieść plik .exe do głównego folderu
"""

# ====== Inicjowanie, wielkość obrazu
pygame.init()
screen_width = 800
screen_hight = 400
screen = pygame.display.set_mode((screen_width, screen_hight))
# ======

# ====== Tytuł, zegar, font
pygame.display.set_caption('Kurwix')
clock = pygame.time.Clock()
terminal_font = pygame.font.Font('Terminal.ttf', 16)
# ======

# ====== Input surface
input_box = pygame.Rect(5, 365, 700, 30)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
last_input = ''
input_available = False
# =======

text_test = ''
add_this = 'Tekst jak terminal. Dodaj tekst, do ustawienia predkosci wyswietlania tekstu.'
i = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # ====== INPUT AREA
        if event.type == pygame.MOUSEBUTTONDOWN and input_available:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                print('ACTIVE')
                active = not active
            else:
                active = False
            # Change the current color of the input box.
        color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = terminal_font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(790, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
    # ======

    if i < len(add_this):
        text_test = text_test + add_this[i]
    elif i == len(add_this):
        print('Koniec wyświetlania')
        input_available = True
    text_surface = terminal_font.render(text_test, True, 'White')
    screen.blit(text_surface, (5, 10))
    i += 1

    pygame.display.update()
    clock.tick(40)  # Pętla while nie działa szybciej niż 60 razy na sekundę. Ogranicznik prędkości gry.
