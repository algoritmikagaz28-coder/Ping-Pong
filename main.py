from pygame import *
from random import randint
from time import time as timer
win_width = 700
win_height = 500
display.set_caption('Пинг-понг')
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('grass_background.png'), (win_width, win_height))
font.init()
font1 = font.SysFont("arial", 80)
font2 = font.SysFont("arial", 20)
font3 = font.SysFont("arial", 10)
text_game_over_r = font1.render('Right player lose!', True, (240,0,0))
text_game_over_l = font1.render('Left player lose!', True, (240,0,0))
text_win_r = font1.render('Right player win!', True, (0, 100, 0))
text_win_l = font1.render('Left player win!', True, (0, 100, 0))
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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
ball_speed_x = 5
ball_speed_y = 5
racketR = Player('racket.png', 655, win_height - 100, 40, 100, 10)
racketL = Player('racket.png', 5, win_height - 100, 40, 100, 10)
ball = GameSprite('ball.png', 330, win_height - 80, 40, 40, 5)
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        racketR.updateR()
        racketR.reset()
        racketL.updateL()
        racketL.reset()
        ball.update()
        ball.reset()
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        if sprite.collide_rect(racketR, ball) or sprite.collide_rect(racketL, ball):
            ball_speed_x *= -1
        if ball.rect.y <= 0 or ball.rect.y >= win_height - 50:
            ball_speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(text_game_over_l, (100,100))
            window.blit(text_win_r, (100,200))
        if ball.rect.x > 660:
            finish = True
            window.blit(text_game_over_r, (100,100))
            window.blit(text_win_l, (100,200))
        display.update()
    time.delay(25)
