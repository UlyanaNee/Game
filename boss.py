import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
WINDOW_WIDTH    = 600
WINDOW_HEIGHT   = 400
WINDOW_SURFACE  = pygame.HWSURFACE|pygame.DOUBLEBUF
bos = pygame.image.load('boos1.png')
bosX = 0
bosY = 200

# Скорость движения объекта
speed = 5


def update(self): #обновления сам
    # Шагайте в текущем направлении
    self.pace_count += 1
    self.rect.x += self.direction * self.pace_size  # Переместите несколько пикселей

    if (self.pace_count >= self.turn_after):
        self.direction *= -1  #изменяет расстояние в пикселях на противоположное
        self.pace_count = 0  # сбросьте количество шагов

    #Мы также должны изменить направление, если коснемся края экрана
    if (self.rect.x <= 0):
        self.direction = 1  # поверните направо
        self.pace_count = 0
    elif (self.rect.x >= WINDOW_WIDTH - self.rect.width):
        self.direction = -1
        self.pace_count = 0
DARK_BLUE = (   3,   5,  54)

class Enemy( pygame.sprite.Sprite ):
    def __init__( self, x, y, pace, bitmap, turn_after=20, speed=100 ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load( bitmap ).convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.center = ( x, y )         # местоположение
        self.pace_size   = pace             # Насколько велик каждый шаг
        self.pace_count  = 0                # расстояние переместилось
        self.direction   = -1               # Начните двигаться влево (-x)
        self.turn_after  = turn_after       # ограничение расстояния
        self.speed       = speed            # Миллисекунды на пакет
        self.pace_time   = 0                # время последнего шага

    def update( self ):
        time_now = pygame.time.get_ticks()               # который сейчас час
        if ( time_now > self.pace_time + self.speed ):
            self.pace_time = time_now

            self.pace_count += 1
            self.rect.x     += self.direction * self.pace_size

            # разворачиваем, если мы прошли достаточно шагов в том же направлении
            if ( self.pace_count >= self.turn_after ):
                # Turn around!
                self.direction *= -1           # изменяет расстояние в пикселях на противоположное
                self.pace_count = 0            # сбросьте количество шагов

            # изменить направление, если коснемся края экрана
            if ( self.rect.x <= 0 ):
                self.direction  = 1             # turn right
                self.pace_count = 0
            elif ( self.rect.x >= WINDOW_WIDTH - self.rect.width ):
                self.direction  = -1
                self.pace_count = 0

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), WINDOW_SURFACE )
pygame.display.set_caption("Movement Algorithm Example")

pos_x = WINDOW_WIDTH//2
pos_y = WINDOW_HEIGHT//2
pace_size = 7
enemy = Enemy( pos_x, pos_y, pace_size, "boos1.png" )

all_sprites_group = pygame.sprite.Group()
all_sprites_group.add( enemy )

clock = pygame.time.Clock()
done = False
while not done:

    # Обрабатывать пользовательский ввод
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            done = True
        elif ( event.type == pygame.MOUSEBUTTONUP ):
            # On mouse-click
            pass
        elif ( event.type == pygame.KEYUP ):
            pass

    all_sprites_group.update()
    window.fill( DARK_BLUE )
    all_sprites_group.draw( window )
    pygame.display.flip()

    clock.tick_busy_loop(60)

pygame.quit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Изменяем значение координаты X
    bosX += speed

    screen.blit(bos, (bosX, bosY))
    pygame.display.update()
    pygame.quit()