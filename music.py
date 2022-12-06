import pygame, map_gen
pygame.init()
pygame.mixer.music.load("NG.mp3")
pygame.mixer.music.play(-1)

score = 0
coin_count = 0
screenX = 850
screenY = 800
screen = pygame.display.set_mode([screenX, screenY])

flPAuse = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPAuse = not flPAuse
                if flPAuse:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
screen = pygame.display.set_mode([850, 850])
pygame.quit()