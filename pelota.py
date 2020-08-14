import pygame
from random import randint

BLACK = 25, 25, 25
WHITE = 250, 250, 250

class Pelota(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super(Pelota, self).__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.velocity = [randint(4, 8), randint(-8, 8)]

		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def rebote(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8, 8)
