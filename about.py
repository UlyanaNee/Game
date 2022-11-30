import pygame
pygame.init()
from  pygame.color import THECOLORS

def drawAbout():
    screenX = 800
    screenY = 600
    screen = pygame.display.set_mode([screenX, screenY])
    run = True
    my_font = pygame.font.SysFont('Calibri', 20 , bold=False, italic=False)
    x = 10
    y = 20
    about_file = open('text.txt', 'r', encoding='utf-8')
    lines = about_file.readlines()
    about_file.close()
    n = len(lines)
    screen.fill(THECOLORS['black'])
    for i in range(n):
        s = lines[i][:-1]
        text = my_font.render(s, True, THECOLORS['cyan'])
        screen.blit(text, [x, y])
        y += 20
    y += 20
    text = my_font.render('', True, THECOLORS['cyan'])
    screen.blit(text, [x, y])
    pygame.display.flip()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.QUIT:
                run = False
    screen = pygame.display.set_mode([640, 640])

pygame.quit()