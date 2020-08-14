import pygame
from pygame.locals import *
from pala import Pala
from pelota import Pelota

pygame.init()

BLACK = 25, 25, 25
WHITE = 250, 250, 250

size = (720, 480)
center_x = (size[0]/2)
center_y = (size[1]/2)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG 1")

pala1 = Pala(WHITE, 10, 100)
pala1.rect.x = 30
pala1.rect.y = center_y - 50

pala2 = Pala(WHITE, 10, 100)
pala2.rect.x = (size[0]-10)-30
pala2.rect.y = center_y - 50

pelota = Pelota(WHITE, 10, 10)
pelota.rect.x = center_x - 5
pelota.rect.y = center_y - 5

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(pala1)
all_sprites_list.add(pala2)
all_sprites_list.add(pelota)

running = True
clock = pygame.time.Clock()

marcador1 = 0
marcador2 = 0

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key==pygame.K_x: #Pressing the x Key will quit the game
				carryOn=False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		pala1.move_up(5)
	if keys[pygame.K_s]:
		pala1.move_down(5)
	if keys[pygame.K_UP]:
		pala2.move_up(5)
	if keys[pygame.K_DOWN]:
		pala2.move_down(5)

	all_sprites_list.update()

	if pelota.rect.x > size[0]-10:
		marcador1 += 1
		pelota.velocity[0] = -pelota.velocity[0]
	if pelota.rect.x <= 0:
		marcador2 += 1
		pelota.velocity[0] = -pelota.velocity[0]
	if pelota.rect.y > size[1]-10:
		pelota.velocity[1] = -pelota.velocity[1]
	if pelota.rect.y  <= 0:
		pelota.velocity[1] = -pelota.velocity[1]

	if pygame.sprite.collide_mask(pelota, pala1) or pygame.sprite.collide_mask(pelota, pala2):
		pelota.rebote()

	screen.fill(BLACK)
	pygame.draw.line(screen, WHITE, [center_x, 0], [center_x, size[1]], 5)
	all_sprites_list.draw(screen)

	font = pygame.font.Font(None, 72)
	text = font.render(str(marcador1), 1, WHITE)
	screen.blit(text, (center_x/2, 10))
	text = font.render(str(marcador2), 1, WHITE)
	screen.blit(text, (center_x + center_x/2, 10))

	pygame.display.flip()

	clock.tick(60)
pygame.quit()

