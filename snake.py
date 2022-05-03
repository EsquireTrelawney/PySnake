# 1 modules connections
import pygame as pg
from random import randrange
# 2 const
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (600, 600)
OBJECT_SIZE = 10
# var-s and init
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
x_coord = randrange(0, WINDOW_WIDTH, OBJECT_SIZE)
y_coord = randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)
body_snake = [(x_coord, y_coord)]
snake_length = 1
dx, dy = 0, 0
fps = 7
apple = randrange(0, WINDOW_WIDTH, OBJECT_SIZE), randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)
# dict for movement directions
traffic_dict = {"W": (0, -1), "S": (0, 1), "A": (-1, 0), "D": (1, 0)}
# init window and closing logic
while True:
    # show screen and fill with black
    screen.fill((200, 127, 127))
    # drawing body snake
    for i, j in body_snake:
        pg.draw.rect(screen, (0, 255, 0), (i, j, OBJECT_SIZE, OBJECT_SIZE))
    pg.draw.rect(screen, (255, 0, 0), (*apple, OBJECT_SIZE, OBJECT_SIZE))
    # coord changes
    x_coord += dx * OBJECT_SIZE
    y_coord += dy * OBJECT_SIZE
    body_snake.append((x_coord, y_coord))
    body_snake = body_snake[-snake_length:]
    # apple eating
    if body_snake[-1] == apple:
        apple = randrange(0, WINDOW_WIDTH, OBJECT_SIZE), randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)
        snake_length += 1
        fps += 1
    # which key was pressed
    key = pg.key.get_pressed()
    # movement conditions
    if key[pg.K_w] and (dx, dy) != traffic_dict['S']:
        dx, dy = traffic_dict["W"]
    if key[pg.K_s] and (dx, dy) != traffic_dict['W']:
        dx, dy = traffic_dict["S"]
    if key[pg.K_a] and (dx, dy) != traffic_dict['D']:
        dx, dy = traffic_dict["A"]
    if key[pg.K_d] and (dx, dy) != traffic_dict['A']:
        dx, dy = traffic_dict["D"]
    # check for border-pass
    if x_coord < 0:
        dx, dy = traffic_dict["D"]
    if x_coord > WINDOW_WIDTH:
        dx, dy = traffic_dict["A"]
    if y_coord < 0:
        dx, dy = traffic_dict["S"]
    if y_coord > WINDOW_HEIGHT:
        dx, dy = traffic_dict["W"]
    # check for cannibalism
    if len(body_snake) != len(set(body_snake)):
        break
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    # screen update
    pg.display.flip()
    # fps control
    clock = pg.time.Clock()
    # amount of times for loop execution
    clock.tick(2*fps)
