#DDA Algorithm
import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((550,550))
pygame.display.set_caption("Anurag Karki DDA Line Drawing Algo")
black=(0,0,0)
screen.fill(black)
white=(255,255,255)
def ROUND(n):
	return int(n+0.5)

def dda(x1,y1,x2,y2):
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)

	for i in range(length):
		x+= dx
		y+= dy
		gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)
	pygame.display.flip()
dda(100,200,400,400)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()



