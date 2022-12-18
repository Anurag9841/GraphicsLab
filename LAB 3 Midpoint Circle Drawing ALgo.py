from pygame import gfxdraw
import sys,pygame
pygame.init()

BLUE = (0, 55, 150)
screen = pygame.display.set_mode((600,600))
screen.fill((10,10,10))
pygame.display.flip()
pygame.display.set_caption("Midpoint circle drawing algorithm")

def circle(radius,offset):
	x,y = 0,radius
	plotCircle(x,y,radius,offset)

# finding the symmetric points using the 8 way symmetry of circle
def symmetry_points(x,y,offset):
	gfxdraw.pixel(screen,x+offset,y+offset,BLUE)
	gfxdraw.pixel(screen,-x+offset,y+offset,BLUE)
	gfxdraw.pixel(screen,x+offset,-y+offset,BLUE)
	gfxdraw.pixel(screen,-x+offset,-y+offset,BLUE)
	gfxdraw.pixel(screen,y+offset,x+offset,BLUE)
	gfxdraw.pixel(screen,-y+offset,x+offset,BLUE)
	gfxdraw.pixel(screen,y+offset,-x+offset,BLUE)
	gfxdraw.pixel(screen,-y+offset,-x+offset,BLUE)
	pygame.display.flip()

def plotCircle(x,y,radius,offset):
	p = 5/4.0 - radius
	symmetry_points(x,y,radius+offset)
	while x < y:
		if p < 0:
			x += 1
			p += 2*x + 1
		else:
			x += 1
			y -= 1
			p += 2*(x-y) + 1
		symmetry_points(x,y,radius+offset)

circle(150,150) # circle(radius,<offset from edge>)
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()