import pygame
pygame.init()
from  pygame.color import THECOLORS
bg_pic = pygame.image.load('fo')
def drawHelp():
    screenX = 800
    screenY = 600
    screen = pygame.display.set_mode([screenX, screenY])
    run = True
    my_font = pygame.font.SysFont('Calibri', 20 , bold=False, italic=False)
    x = 10
    y = 20
    help_file = open('prava.txt', 'r', encoding='utf-8')
    lines = help_file.readlines()
    help_file.close()
    n = len(lines)
    screen.fill(THECOLORS['navy'])
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.QUIT:
                run = False
    screen = pygame.display.set_mode([640, 640])

pygame.quit()