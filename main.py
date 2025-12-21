from pygame import *
from random import randint
from time import time as timer
win_width = 700
win_height = 500
lost = 0
destroed = 0
max_lost = 3
need_destroy = 11
display.set_caption('Пинг-понг')
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('grass_background.png'), (win_width, win_height))
font.init()
font1 = font.SysFont("arial", 80)
font2 = font.SysFont("arial", 20)
font3 = font.SysFont("arial", 10)
text_game_over_r = font1.render('Right player lose!', True, (240,0,0))
text_game_over_l = font1.render('Left player lose!', True, (240,0,0))
text_win_r = font1.render('Right player win!', True, (0,240,0))
text_win_l = font1.render('Left player win!', True, (0,240,0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 85:
            self.rect.x += self.speed
        def updateR(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.x < win_width - 85:
            self.rect.x += self.speed
racketR = Player('racket.png', 5, win_height - 100, 80, 100, 10)
racketL = Player('racket.png', 5, win_height - 100, 80, 100, 10)
ball = GameSprite('It_is _not_a_circle.', 5, win_height, 80, 5, 10)
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        ball.update()
        ball.reset()
        racketR.updateR()
        racketR.reset()
        racketL.updateL()
        racketL.reset()
        if sprite.spritecollide(racketR, ball, False) or sprite.spritecollide(racketL, ball, False):
            finish = True
            window.blit(text_game_over, (230, 200))
        if destroed >= need_destroy:
            finish = True
            window.blit(text_win, (230, 200))
        display.update()
    time.delay(25)