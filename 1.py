import pygame
import pygame.freetype  # Import the freetype module.


pygame.init()

screen = pygame.display.set_mode((640, 240))

sysfont = pygame.font.get_default_font()

font = pygame.font.SysFont(None, 48)

img = font.render('hello', True, (255, 0, 0))

background = (112, 112, 112)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    screen.blit(img, (20, 20))
    pygame.display.update()

pygame.quit()