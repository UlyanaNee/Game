my_score = 0

screenX = 850
screenY = 800
dx = 2
dy = 2
yr = 200
xr = 750
w = 30
h = 200
color = THECOLORS['lightblue']

#тут нужно прописать

my_delay = 50
interval = 50

while run == True:
    screen.fill(THECOLORS['white'])
    screenX , screenY, dx, dy = moveMap(screenX, screenY , dx , dy , color)  #вызов функция
    pygame.time.delay(10)
    dx, my_score = check(screenX, screenY, dx, my_score)
    text = my_font.render('Счёт:' + str (my_score), True , THECOLORS['blue'])
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            yr = more_r(yr, step)
    pygame.draw.rect(screen, THECOLORS['green'], [xr, yr, w, h],0)
    screen.blit(text, [250 , 50])


    #или

Length_of_player = 1  #ставим после def

def Your_score(score):
   value = score_font.render("Ваш счёт: " + str(score), True, yellow)
   dis.blit(value, [0, 0])
   Your_score(Length_of_player - 1)
