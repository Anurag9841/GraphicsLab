import pygame
import math
import pygame.gfxdraw

# Screen Dimensions
HEIGHT = 900
WIDTH = 1100

# Screen Colors
WHITE = (255, 255, 255)
RED = (220, 30, 70)
BLUE = (0, 56, 147)
BLACK=(0,0,0)

PI = math.pi

def prepare_screen():
    """
    Create the viewing  screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    pygame.display.set_caption("Anurag Karki Flag Of Nepal")
    return screen

A =(500,500)
B = (500, 50)
C = (900,300)
D=(650,300)
E = (900,550)
F = (500, 550)


def draw_skeleton():
    """Outline of flag"""
    AB = pygame.draw.polygon(screen, BLUE, [A, B, C, D, E, F], 10)

def draw_inner_part():
    AC = pygame.gfxdraw.filled_polygon(screen, [A, B, C, D, E, F], RED)



def rotation(point1, point2, angle):
    """Rotate the point1 around point2 with given angle."""
    x, y = point1[0], point1[1]
    a, b = point2[0], point2[1]
    return (math.cos(angle) * (x - a) - math.sin(angle) * (y - b) + a, math.sin(angle) * (x - a) 
            + math.cos(angle) * (y - b) + b)


def draw_triangles_round(n, height, startpoint, base_length, angle):
    """Draw the Triangles around Sun and Moon to look them Like Sun and Moon"""
    for i in range(n):
        endpoint = (startpoint[0], startpoint[1] - base_length)
        outer_point = (startpoint[0] + height,
                       startpoint[1] - base_length/2)
        rotated_end_point = rotation(endpoint, startpoint, -(i * (angle)))
        rotated_outer_point = rotation(
            outer_point, startpoint, -(i * (angle)))
        initial_poly = pygame.draw.polygon(
            screen, WHITE, (startpoint, rotated_end_point, rotated_outer_point))
        startpoint = rotated_end_point




screen = prepare_screen()
draw_inner_part()
draw_skeleton()
pygame.draw.circle(screen, WHITE, [600, 420], 50)
pygame.draw.circle(screen, WHITE, [599, 220], 70)
pygame.draw.circle(screen, RED, [599, 200], 70)

base_length_sun = 25
startpoint_sun = (598 + 50, 420 + base_length_sun/2)

draw_triangles_round(15, 12,startpoint_sun, base_length_sun, PI/6)

angle = math.radians(360/18)
base_length_moon = 17.5
startpoint_moon = (599 + 50 - 0.52, 240 + base_length_moon/2 + 1)
draw_triangles_round(10, 12, startpoint_moon,base_length_moon, angle)
pygame.draw.circle(screen, WHITE, [599, 240], 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            quit()
    pygame.display.update()