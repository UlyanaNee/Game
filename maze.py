import pygame, map_gen
pygame.init()


def drawGame():

    score = 0
    coin_count = 0
    screenX = 640
    screenY = 640
    dx = 64
    dy = 64
    playernew = pygame.image.load('player.png')
    player =pygame.transform.scale(playernew, (dx, dy))
    wall = pygame.image.load('wall.jpg')
    road = pygame.image.load('road.jpg')
    prize = pygame.image.load('prize.png')
    door = pygame.image.load('door.jpg')


    N = 10
    M = 10
    map_list = [0] * N
    for i in range(N):
        map_list[i] = [0]*M

    def readFile(file_path, map_list, flag = 0):
        count = 0
        if flag == 0:
            map_file = open(file_path, 'r')
        else:
            map_gen.main()
            map_file = open('map_gen.txt', 'r')
        s = map_file.readline()
        s = s.split()
        N, M = int(s[0]), int(s[1])
        for i in range(N):
            s = map_file.readline()
            s = s.split()
            for j in range(M):
                map_list[i][j] = int(s[j])
                if map_list[i][j] == 3:
                    count += 1
                print(map_list[i][j], end=" ")
            print()
        map_file.close()
        return (map_list, count,N, M)
    screen = pygame.display.set_mode([screenX, screenY])
    run = True
    # 'w' перезапись файла
    # 'a' дозапись в конец файла

    def drawMap():
        player_i, player_j = 0, 0
        for i in range(N):
            for j in range(N):
                x = dx * j
                y = dy * i
                if (map_list[i][j] == 0): #стена
                    screen.blit(wall, [x, y])
                elif (map_list[i][j] == 1): #дорога
                    screen.blit(road,[x, y])
                elif (map_list[i][j] == 2): # персонаж
                    screen.blit(road, [x, y])
                    screen.blit(player,[x, y])
                    player_i = i #строка
                    player_j = j #столбик
                elif (map_list[i][j] == 3):  #монетка
                    screen.blit(prize, [x, y])
                elif (map_list[i][j] == 4):  #дверь
                    screen.blit(door, [x, y])
        return  (player_i, player_j)

    def analysis_key(player_i, player_j, new_i, new_j):
        if event.key == pygame.K_UP:
            if player_i - 1 >= 0:
                new_i = player_i - 1
        elif event.key == pygame.K_DOWN:
            if player_i + 1 < N:
                new_i = player_i + 1
        elif event.key == pygame.K_LEFT:
            if player_j - 1 >= 0:
                new_j = player_j - 1
        elif event.key == pygame.K_RIGHT:
            if player_j + 1 < N:
                new_j = player_j + 1
        return (new_i, new_j)
    score = 0
    prizeCount = 3


    def moveMap(player_i, player_j, new_i, new_j, map_list, score,prizeCount,level, N, M):
        if (map_list[new_i][new_j] == 0):
            new_i = player_i
            new_j = player_j
        elif map_list[new_i][new_j] == 1:
            map_list[player_i][player_j] = 1
            map_list[new_i][new_j] = 2
            player_i = new_i
            player_j = new_j
        elif map_list[new_i][new_j] == 3:
            map_list[player_i][player_j] = 1
            map_list[new_i][new_j] = 2
            player_i = new_i
            player_j = new_j
            score += 1
        elif map_list[new_i][new_j] == 4:
            if score == prizeCount:
                map_list[player_i][player_j] = 1
                map_list[new_i][new_j] = 2
                player_i = new_i
                player_j = new_j
                level += 1
                if level <= 3:
                    map_list, prizeCount, N, M = readFile('karta' + str(level)+'.txt', map_list, 0)
                else:
                    map_list, prizeCount, N, M = readFile(None, None, 1)

                score = 0
            else:
                new_i = player_i
                new_j = player_j
        return (player_i, player_j, new_i, new_j,score,prizeCount, level, N, M)
    my_delay = 100
    interval = 50
    pygame.key.set_repeat(my_delay, interval)
    player_i = 0 #координат персонаж в матрице
    player_j = 0
    new_i = 0 #кординаты клетки, куда персонаж хочет походить
    new_j = 0
    level = 1
    map_list, prizeCount, N, M = readFile('karta1.txt', map_list, 0)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                new_i, new_j = analysis_key(player_i, player_j, new_i, new_j)
                player_i, player_j, new_i, new_j, score, prizeCount, level, N, M = moveMap(player_i, player_j, new_i, new_j, map_list, score, prizeCount,level, N, M)
        player_i, player_j = drawMap()
        pygame.display.flip()
    screen = pygame.display.set_mode([640, 640])
    #pygame.quit()

