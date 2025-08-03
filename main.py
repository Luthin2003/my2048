import pygame
import random
import math
import movement
import copy

pygame.init()

FPS = 60

WIDTH ,HEIGHT = 800 , 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT//ROWS
RECT_WIDTH = HEIGHT//COLS

OUTLINE_COLOR = (187 , 173 , 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205 , 192 , 180)
FONT_COLOR = (119 , 110 , 101)

FONT = pygame.font.SysFont("comicsans" , 60 , bold = True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237 , 229 , 218),
        (238 , 225 , 201),
        (243 , 178 , 122),
        (246 , 150 , 101),
        (247 , 124 , 95),
        (247 , 95 , 59),
        (237 , 208 , 115),
        (237 , 204 , 99),
        (236 , 202 , 80),
        (237, 197, 47),  
        (60, 58, 50),    
        (30, 28, 20),     
    ]

    def __init__(self , value , row , col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col*RECT_WIDTH
        self.y = row*RECT_HEIGHT

    def get_color(self):
        return self.COLORS[int(math.log2(self.value)) - 1]

    def draw(self , window):
        color = self.get_color()
        pygame.draw.rect(window , color , (self.x , self.y , RECT_WIDTH , RECT_HEIGHT))
        text = FONT.render(str(self.value) , 1 , FONT_COLOR)
        window.blit(
            text ,
            (
                self.x + (RECT_WIDTH/2 - text.get_width()/2),
                self.y + (RECT_HEIGHT/2 - text.get_height()/2),
            )
        )


    def move(self , delta):
        pass

    def set_pos(self):
        pass


def draw_grid(window):
    for row in range(1 , ROWS):
        y = row*RECT_HEIGHT

        pygame.draw.line(window , OUTLINE_COLOR , (0 , y) , (WIDTH , y) , OUTLINE_THICKNESS)
    
    for col in range(1 , COLS):
        x = col*RECT_WIDTH

        pygame.draw.line(window , OUTLINE_COLOR , (x , 0) , (x , HEIGHT) , OUTLINE_THICKNESS)


    pygame.draw.rect(window , OUTLINE_COLOR , (0 , 0 , WIDTH , HEIGHT) , OUTLINE_THICKNESS)



def draw(window , tiles):
    window.fill(BACKGROUND_COLOR)
# drawing tiles

    for rows in tiles:
        for tile in rows:
            if tile.value != 0:
                tile.draw(window) 

#drawing grid
    draw_grid(window)
    pygame.display.update()

def get_random_pos(tiles):

    row = None
    col = None

    while True:
        row = random.randrange(0 , ROWS)
        col = random.randrange(0 , COLS)

        if tiles[row][col].value == 0:
            break

    return row , col

def generate_tiles():
    tiles = []

    for i in range(ROWS):
        rows = []
        for j in range(COLS):
            rows.append(Tile(0 , i , j))
        tiles.append(rows)

    for _ in range(2):
        row , col = get_random_pos(tiles)
        tiles[row][col] = Tile(2 , row , col)

    return tiles

def generate_tile_after(tiles):

    row , col = get_random_pos(tiles)
    value = 2 if random.randrange(0, 2) == 0 else 4
    tiles[row][col] = Tile(value , row , col)
    return tiles


def end_tiles(tiles):

    isempty = False
    for rows in tiles:
        for tile in rows:
            if tile.value == 0:
                isempty = True


    return isempty


def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                ismove = None
                if event.key == pygame.K_LEFT:
                    ismove = movement.LEFT_MOVEMENT(tiles ,ROWS , COLS)
                elif event.key == pygame.K_RIGHT:
                    ismove = movement.RIGHT_MOVEMENT(tiles ,ROWS , COLS)
                elif event.key == pygame.K_UP:
                    ismove = movement.UP_MOVEMENT(tiles ,ROWS , COLS)
                elif event.key == pygame.K_DOWN:
                    ismove = movement.DOWN_MOVEMENT(tiles ,ROWS , COLS)

                if ismove == True:
                    tiles = generate_tile_after(tiles)

                ismove = None
            
        isempty  = end_tiles(tiles)
        
        draw(window , tiles)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)