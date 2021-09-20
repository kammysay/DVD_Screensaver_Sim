# Iconic DVD Logo Screen Saver Simulator
# github.com/kammysay/DVD_Screensaver_Sim

import os
import pygame as pg
import random as rdm

pg.init()

# WINDOW
WIDTH, HEIGHT = 1920, 1080
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# COLORS
BLACK = (0, 0, 0)

# LOGO STUFF
L_WIDTH, L_HEIGHT = 200, 100
LOGO_IMG = pg.image.load(
    os.path.join('images', 'dvd.png'))
LOGO_RECT = pg.transform.rotate(
    pg.transform.scale(LOGO_IMG, (L_WIDTH, L_HEIGHT)), 0)

# Class that holds all information about the logo object
class Logo():
    def __init__(self, width, height, x, y):
        # Rectangle fields
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        
        # General class information
        self.dir_x = 1 # 0 Left, 1 Right
        self.dir_y = 1 # 0 Up, 1 Down
        self.vel_x = 2 # Velocity AKA how many pixels it moves every frame
        self.vel_y = 2 # Velocity AKA how many pixels it moves every frame

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    # Flip the value of dir_x
    def flip_x_dir(self):
        if self.dir_x == 0:
            self.dir_x = 1
            self.vel_x = 2
        elif self.dir_x == 1:
            self.dir_x = 0
            self.vel_x = -2

    # Flip the value of dir_y
    def flip_y_dir(self):
        if self.dir_y == 0:
            self.dir_y = 1
            self.vel_y = 2
        elif self.dir_y == 1:
            self.dir_y = 0
            self.vel_y = -2
        
# Draw everything to the screen
def draw_window(logo):
    WIN.fill(BLACK)
    WIN.blit(LOGO_RECT, (logo.rect.x, logo.rect.y))
    pg.display.update()

# Move the logo and adjust direction if necessary
def move_logo(logo):
    logo.move()

    # Check for x collisions
    if logo.rect.left <= 0:
        logo.flip_x_dir()
    if logo.rect.right >= WIDTH:
        logo.flip_x_dir()
    
    # Check for y collisions
    if logo.rect.top <= 0:
        logo.flip_y_dir()
    if logo.rect.bottom >= HEIGHT:
        logo.flip_y_dir()

def main():
    # Generate the logos starting point, init logo
    # x, y, = 1000, 500     # Corner hit within the first couple of bounces :)
    x, y = rdm.randrange(0, WIDTH-L_WIDTH), rdm.randrange(0, HEIGHT-L_HEIGHT) # Random starting point
    logo = Logo(L_WIDTH, L_HEIGHT, x, y)

    # Main game loop
    clock = pg.time.Clock()
    while True:
        clock.tick(FPS)
        keys_pressed = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT or keys_pressed[pg.K_ESCAPE]:
                pg.quit()

        move_logo(logo)
        draw_window(logo)

if __name__ == "__main__":
    main()