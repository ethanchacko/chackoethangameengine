# This file was made by: Ethan Chacko
#Content from Chris Bradfield; Kids can code
#KidsCanCode - Game Development with pygame video series

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from setting import *
from sprites import *
 
vec = pg.math.Vector2
 
# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
 
 
 

 
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)
 
# Capital letter is a convention for creating a class
# Sprite is a superclass
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        # use an image for player sprite...
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # self.rect.x += 5
        # self.rect.y += 5
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # hits = pg.sprite.spritecollide(self, all_platforms, False)
        # if hits:
        #     print("i've collided...")
        # if friction - apply here
        self.acc.x += self.vel.x * -0.5
        self.acc.y += self.vel.y *-0.1
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.1 * self.acc
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        self.rect.midbottom = self.pos
 
# platforms
 

 
for p in PLATFORM_LIST:
    # Instantiation of the Platform class
    plat = Platform(*p)
    all_sprites.add(plat)
    all_platforms.add(plat)
 
for m in range(0,25):
    m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
    all_sprites.add(m)
    all_mobs.add(m)
 
# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
       
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
   
    ############ Update ##############
    # update all sprites
    all_sprites.update()
 
    # this is what prevents the player from falling through the platform when falling down...
    if player.vel.y > 0:
            hits = pg.sprite.spritecollide(player, all_platforms, False)
            if hits:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
               
    # this prevents the player from jumping up through a platform
    if player.vel.y < 0:
        hits = pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
            print("ouch")
            SCORE -= 1
            if player.rect.bottom >= hits[0].rect.top - 5:
                player.rect.top = hits[0].rect.bottom
                player.acc.y = 5
                player.vel.y = 0
 
    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)
    draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)
 
    # buffer - after drawing everything, flip display
    pg.display.flip()
 
pg.quit()
 