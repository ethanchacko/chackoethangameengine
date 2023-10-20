# This file was made by: Ethan Chacko

#Content from Chris Bradfield; Kids can code
#KidsCanCode - Game Development with pygame video series
 
 
# game settings

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
 
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 

 
vec = pg.math.Vector2

WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0
 
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
 
PLATFORM_LIST =  [(0, HEIGHT - 40, WIDTH, 40, "normal"),              
                  (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "moving"),
                  (125, HEIGHT - 350, 100, 20, "normal"),
                  (350, 200, 100, 20, "moving"),
                  (175, 100, 50, 20, "normal")]