import pygame

BLACK = 25, 25, 25
WHITE = 250, 250, 250

class Pala(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super(Pala, self).__init__()
		self.height = height
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.rect = self.image.get_rect()


	def move_up(self, pixels):
		self.rect.y -=pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def move_down(self, pixels):
		self.rect.y +=pixels
		if self.rect.y > 480 - self.height:
			self.rect.y = 480 - self.height