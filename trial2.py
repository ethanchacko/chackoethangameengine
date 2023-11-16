# This file was created by: Ethan Chacko 

'''
Sources:

content from kids can code: http://kidscancode.org/blog/

content from: https://www.geeksforgeeks.org/create-a-pong-game-in-python-pygame/
Things that I modified from the orignal:
Changed the game so that is is now veritical instead of horizontal
Made some slight color modifications
Adjusted the dimensions of the window and the positions of where objects should be
Made the game single player, by creating Artificial Stupidity

Tasks that I am in the process of and one that I aim to complete:

Fixing the glitching on the right hand of the screen(In Progress)
Making the code Modular(In Progress)
Making the Player be able to choose where the want to hit the ball
Have the Computer also decides where is hits the Ball

'''


# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os  
import math


pg.init()
 
# The Font
font20 = pg.font.Font('freesansbold.ttf', 20)
 
# Defining the colors and their values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
 
# Setting the basic parameters of the screen
WIDTH, HEIGHT = 600, 720
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
# Used to adjust the frame rate
clock = pg.time.Clock()
FPS = 90

# Creating the Player class

class Player: 
    # Defining the Player
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pg.Rect(posx, posy, width, height)
        # Object that is shown on the screen
        self.rect = pg.draw.rect(screen, self.color, self.rect)
 
    # Used to display the object on the screen
    def display(self):
        self.show = pg.draw.rect(screen, self.color, self.rect)

    # Defining the state of the object
    def update(self, xvel):
        self.posx = self.posx + self.speed*xvel
 
        # Restricting the Player so that it can't travel out of bounds
        if self.posx <= 0:
            self.posx = 0
      
        elif self.posx + self.height >= WIDTH:
            self.posx = WIDTH-self.width
 
        # Updating the rect with the new values
        self.rect = (self.posx, self.posy, self.width, self.height)

# Used to render the score on to the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.rect
    
# Creating the Computer Class
# Artifical Stupidity :)

class Computer: 
    # Defining the Computer
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pg.Rect(posx, posy, width, height)
        # Object that is shown on the screen
        self.rect = pg.draw.rect(screen, self.color, self.rect)
 
    # Used to display the object on the screen
    def display(self):
        self.show = pg.draw.rect(screen, self.color, self.rect)

    # Defining the state of the object
    def update(self, xvel, ball):
        if self.posx < ball.posx:
            xvel += 1
        if self.posx > ball.posx:
            xvel -= 1
        self.posx = self.posx + self.speed*xvel
 
        # Restricting the Computer so that it can't exceed the boundries
        if self.posx <= 0:
            self.posx = 0
        
        elif self.posx + self.height >= WIDTH:
            self.posx = WIDTH-self.width
 
        # Updating the rect with the new values
        self.rect = (self.posx, self.posy, self.width, self.height)

# Used to render the score on to the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.rect
    
#Creating the Ball class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xvel = 1
        self.yvel = -1
        self.ball = pg.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
 
    def display(self):
        self.ball = pg.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
    
    def update(self):
        self.posx += self.speed*self.xvel
        self.posy += self.speed*self.yvel

        # Making the ball bounce/reflect of the walls
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xvel *= -1

        # Making sure that the program adustss the score when someone scores
        if self.posy <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posy >= HEIGHT and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
        

# Used to reset the position of the ball to the center of the screen
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.yvel *= -1
        self.firstTime = 1
 
    # Used to reflect the ball along the Y-axis
    def hit(self):
        self.yvel *= -1
 
    def getRect(self):
        return self.ball
    


# Game Manager
def main():
    running = True
 
    # Defining the objects
    p1 = Player(220, 50, 100, 10, 10, WHITE)
    p2 = Computer(320, 650, 100, 10, 10, WHITE)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

    listOfPlayers = [p1, p2]
 
    
    # Initial parameters of the Player and Computer
    p1Score, p2Score = 0, 0
    p1xvel, p2xvel = 0, 0
 
    while running:
        screen.fill(BLACK)

    # Event handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    p2xvel = -1
                if event.key == pg.K_RIGHT:
                    p2xvel = 1
                if event.key == pg.K_a:
                    p1xvel = -1
                if event.key == pg.K_d:
                    p1xvel = 1
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    p2xvel = 0
                if event.key == pg.K_d or event.key == pg.K_a:
                    p1xvel = 0

        # Collision detection
        for p in listOfPlayers:
            if pg.Rect.colliderect(ball.getRect(), p.getRect()):
                ball.hit()
 
        # Updating the objects
        p1.update(p1xvel)
        p2.update(p2xvel, ball)
        point = ball.update()

        # -1 -> The Player has scored
        # +1 -> The Computer has scored
        #  0 -> None of them scored
        if point == -1:
            p1Score += 1
        elif point == 1:
            p2Score += 1
 
         # Reseting the Ball when someone scores a point
        if point:   
            ball.reset()
 
        # Displaying the objects on the screen
        p1.display()
        p2.display()
        ball.display()
 
        # Displaying the scores of the players
        p1.displayScore("Player : ", p1Score, 100, 20, WHITE)
        p2.displayScore("Computer : ", p2Score, WIDTH-100, 20, WHITE)
 
        pg.display.update()
        # Adjusting the frame rate
        clock.tick(FPS)
                    

if __name__ == "__main__":
    main()
    pg.quit()