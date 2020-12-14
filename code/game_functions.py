import pygame
from pygame.locals import *  # noqa
import sys
import random


def birdUpdate(jump, jumpSpeed, birdY, gravity, bird, wallx,
			   gap, offset, wallUp, wallDown, dead, counter):
	if jump:
		jumpSpeed -= 1
		birdY -= jumpSpeed
		jump -= 1
	else:
		birdY += gravity
		gravity += 0.2
	bird[1] = birdY
	upRect = pygame.Rect(wallx,
						 360 + gap - offset + 10,
						 wallUp.get_width() - 10,
						 wallUp.get_height())
	downRect = pygame.Rect(wallx,
						   0 - gap - offset - 10,
						   wallDown.get_width() - 10,
						   wallDown.get_height())
	if upRect.colliderect(bird):
		dead = True
	if downRect.colliderect(bird):
		dead = True
	if not 0 < bird[1] < 720:
		bird[1] = 50
		birdY = 50
		dead = False
		counter = 0
		wallx = 400
		offset = random.randint(-110, 110)
		gravity = 5 


def run(jump, gravity, jumpSpeed, screen, background, wallUp,
		wallx, gap, offset, wallDown, dead, sprite, birdSprites,
		birdY):
	clock = pygame.time.Clock()
	pygame.font.init()
	font = pygame.font.SysFont("Arial", 50)
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
				jump = 17
				gravity = 5
				jumpSpeed = 10

		screen.fill((255, 255, 255))
		screen.blit(background, (0, 0))
		screen.blit(wallUp,
						(wallx, 360 + gap - offset))
		screen.blit(wallDown,
						(wallx, 0 - gap - offset))
		screen.blit(font.render(str(self.counter),
									 -1,
									 (255, 255, 255)),
						(200, 50))
		if dead:
			sprite = 2
		elif jump:
			sprite = 1
		screen.blit(birdSprites[sprite], (70, birdY))
		if not dead:
			sprite = 0
		updateWalls()
		birdUpdate()
		pygame.display.update()