import pygame, maze, help, about
pygame.init()
pygame.mixer.music.load("NG.mp3")
pygame.mixer.music.play(-1)

from  pygame.color import THECOLORS
my_font = pygame.font.SysFont('Calibri', 40, bold=False, italic=False)
top = [60,210,360]
left = 100
width = 200
height = 80
menu_text = ['Game', 'Help', 'About']
screenX = 850
screenY = 800
screen = pygame.display.set_mode([screenX, screenY])
bg_pic = pygame.image.load('font1.png')
bg = pygame.transform.scale(bg_pic,(850 , 800) )
run = True
while run :
    #screen.fill(THECOLORS['navy'])
    screen.blit(bg, [0, 0])
    for i in range(3):
        pygame.draw.rect(screen, THECOLORS['cyan'],[left, top[i],width, height])
        text = my_font.render(menu_text[i], True, THECOLORS['navy'])
        screen.blit(text, [left + 50, top[i] + 30])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            for k in range(3):
                if x > left and x < left + width and y > top[k] and y < top[k] + height:
                    break
                else:
                    k = 10   #создаём кнопки
            if k == 0:
                print('Game')
                maze.drawGame(my_font)
            elif k == 1:
                print('Help')
                help.drawHelp()
            elif k == 2:
                print('About')
                about.drawAbout()

    pygame.display.flip()
pygame.quit()