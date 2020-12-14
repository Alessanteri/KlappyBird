import pygame
from pygame.locals import *  # noqa
import sys
import random
import time

from background import Background


class Bird(Background):

	def bird_update(self):
		if self.jump:
			self.jumpSpeed -= 1
			self.birdY -= self.jumpSpeed
			self.jump -= 1
		else:
			self.birdY += self.gravity
			self.gravity += 0.2
		self.bird[1] = self.birdY
		upRect = pygame.Rect(self.wallx,
							 360 + self.gap - self.offset + 10,
							 self.wallUp.get_width() - 10,
							 self.wallUp.get_height())
		downRect = pygame.Rect(self.wallx,
							   0 - self.gap - self.offset - 10,
							   self.wallDown.get_width() - 10,
							   self.wallDown.get_height())
		if upRect.colliderect(self.bird):
			self.dead = True
		if downRect.colliderect(self.bird):
			self.dead = True
		if not 0 < self.bird[1] < 597:
			self.bird[1] = 50
			self.birdY = 50
			self.dead = False
			self.writeFile(self.counter)
			self.end_game(self.counter)
			self.counter = 0
			self.wallx = 400
			self.offset = random.randint(-50, 310)
			self.gravity = 5


	def end_game(self, count):
		area_start = pygame.Rect(148, 447, 100, 35)
		area_exit = pygame.Rect(148, 492, 100, 35)
		font = pygame.font.SysFont("Arial", 35)
		clock = pygame.time.Clock()
		while True:
			clock.tick(60)
			pygame.display.update()
			self.screen.blit(self.score_table, (59, 160))
			self.screen.blit(font.render(str(count),	
										 -1,
										 (255, 255, 255)),
										 (275, 193))
			totalScore = self.readFile()
			self.screen.blit(font.render(str(totalScore),	
										 -1,
										 (255, 255, 255)),
										 (267, 248))
			self.screen.blit(self.start, (148,447))
			self.screen.blit(self.exit, (148, 492))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if (event.type == pygame.KEYDOWN):
					if event.key == pygame.K_ESCAPE:
						#time.sleep(0.3)
						return 0
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if area_start.collidepoint(event.pos):
							self.counter = 0
							self.wallx = 400
							self.offset = random.randint(-50, 310)
							self.gravity = 5
							self.run()
						elif area_exit.collidepoint(event.pos):
							self.counter = 0
							self.wallx = 400
							self.offset = random.randint(-50, 310)
							self.gravity = 5
							self.start_menu()



	