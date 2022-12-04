import pygame

pygame.init()
from pygame.color import THECOLORS


def drawHelp():
    bg_pic = pygame.image.load('font2.png')
    bg = pygame.transform.scale(bg_pic, (850, 800))
    screenX = 850
    screenY = 800
    screen = pygame.display.set_mode([screenX, screenY])
    run = True
    my_font = pygame.font.SysFont('Calibri', 20, bold=False, italic=False)
    x = 10
    y = 20
    help_file = open('prava.txt', 'r', encoding='utf-8')
    lines = help_file.readlines()
    help_file.close()
    n = len(lines)
    # screen.fill(THECOLORS['navy'])
    screen.blit(bg, [0, 0])
    for i in range(n):
        s = lines[i][:-1]
        text = my_font.render(s, True, THECOLORS['cyan'])
        screen.blit(text, [x, y])
        y += 20
    y += 20
    text = my_font.render('Для возврата в меню нажмите любую клавищу', True, THECOLORS['cyan'])
    screen.blit(text, [x, y])
    pygame.display.flip()
    while run:
        screen.blit(bg, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.QUIT:
                run = False
    screen = pygame.display.set_mode([850, 800])


pygame.quit()