import pygame
from pygame.locals import *  # noqa
import sys
import random
import time

from bird import Bird 


class KlappyBird(Bird):
	def start_menu(self):
		#self.screen.fill((255, 255, 255)) 
		area_style = pygame.Rect(148, 402, 100, 35)
		area_start = pygame.Rect(148, 357, 100, 35)
		area_score = pygame.Rect(148, 447, 100, 35)
		#area_menu = pygame.Rect(148, 492, 100, 35)
		area_exit = pygame.Rect(148, 492, 100, 35)
		clock = pygame.time.Clock()
		while True:
			clock.tick(60)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						#self.screen.fill((255, 255, 255))
						self.run()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if area_style.collidepoint(event.pos):	
							self.choice_bird()
						elif area_start.collidepoint(event.pos):
							self.run()
						elif area_score.collidepoint(event.pos):
							pass
						#self.score()
						# elif area_menu.collidepoint(event.pos):
						# #self.start_menu()
							self.scoreGame()
						elif area_exit.collidepoint(event.pos):
							sys.exit()

			self.screen.fill((255, 255, 255))
			self.screen.blit(self.background, (-1, 0))
			self.screen.blit(self.base, (self.baseX, 597))
			self.screen.blit(self.message, (106, 60))
			self.screen.blit(self.start, (148, 357))
			self.screen.blit(self.style, (148, 402))
			self.screen.blit(self.score, (148, 447))
			#self.screen.blit(self.menu, (148, 492))
			self.screen.blit(self.exit, (148,492))


	def choice_bird(self):
		area_yellow_bird = pygame.Rect(45, 50, 100, 35)
		area_red_bird = pygame.Rect(45, 120, 100, 35)
		area_blue_bird = pygame.Rect(45, 190, 100, 35)
		area_menu = pygame.Rect(148, 492, 100, 35)
		area_back = pygame.Rect(148, 537, 100, 35)
		area_day = pygame.Rect(45, 480, 100, 35)
		area_night = pygame.Rect(250, 480, 100, 35)
		clock = pygame.time.Clock()
		self.yellowBirdPress = self.yellowBird
		self.redBirdPress = self.redBird
		self.blueBirdPress = self.blueBird
		self.dayPressed = self.day
		self.nightPressed = self.night
		while True:
			clock.tick(60)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.run()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						# if area_menu.collidepoint(event.pos):	
						# 	self.start_menu()
						if area_back.collidepoint(event.pos):
							self.start_menu()
						elif area_yellow_bird.collidepoint(event.pos):
							self.yellowBirdPress = self.yellowBirdPressed
							self.redBirdPress = self.redBird
							self.blueBirdPress = self.blueBird
							self.birdStyle = self.yellowBirdSprites
						elif area_red_bird.collidepoint(event.pos):
							self.yellowBirdPress = self.yellowBird
							self.redBirdPress = self.redBirdPressed
							self.blueBirdPress = self.blueBird
							self.birdStyle = self.redBirdSprites
						elif area_blue_bird.collidepoint(event.pos):
							self.yellowBirdPress = self.yellowBird
							self.redBirdPress = self.redBird
							self.blueBirdPress = self.blueBirdPressed
							self.birdStyle = self.blueBirdSprites
						elif area_day.collidepoint(event.pos):
							self.dayPressed = self.dayPress
							self.nightPressed = self.night
							self.background = self.backgroundDay
						elif area_night.collidepoint(event.pos):
							self.dayPressed = self.day
							self.nightPressed = self.nightPress
							self.background = self.backgroundNight

			self.screen.fill((255, 255, 255))
			self.screen.blit(self.background, (-1, 0))
			self.screen.blit(self.base, (self.baseX, 597))
			#self.screen.blit(self.menu, (148, 492))
			self.screen.blit(self.back, (148, 537))
			self.screen.blit(self.yellowBirdPress, (45, 50))
			self.screen.blit(self.yellowBirdSprites[3], (170, 50))	
			self.screen.blit(self.redBirdPress, (45, 120))
			self.screen.blit(self.redBirdSprites[3], (170, 120))
			self.screen.blit(self.blueBirdPress, (45, 190))
			self.screen.blit(self.blueBirdSprites[3], (170, 190 ))
			#self.screen.blit(self.table, (0, 300))
			self.screen.blit(self.bd, (30, 320))
			self.screen.blit(self.dayPressed, (45, 480))
			self.screen.blit(self.nightPressed, (250, 480))


	def run(self):
		clock = pygame.time.Clock()
		pygame.font.init()
		font = pygame.font.SysFont("Arial", 50)
		while True:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if (event.type == pygame.KEYDOWN) and not self.dead:
					if event.key == pygame.K_SPACE:
						self.jump = 17
						self.gravity = 5
						self.jumpSpeed = 10
					if event.key == pygame.K_ESCAPE:
						self.pauseGame()
						time.sleep(0.3)

			self.screen.fill((255, 255, 255)) 
			self.screen.blit(self.background, (-1, 0))
			self.screen.blit(self.wallUp,
							 (self.wallx, 360 + self.gap - self.offset))
			self.screen.blit(self.wallDown,
							 (self.wallx, 0 - self.gap - self.offset))
			self.screen.blit(self.base, (self.baseX, 597))
			self.screen.blit(font.render(str(self.counter),	
										 -1,
										 (255, 255, 255)),
										 (200, 50))
			if self.dead:
				self.sprite = 2
			elif self.jump:
				self.sprite = 1
			self.screen.blit(self.birdStyle[self.sprite], (70, self.birdY))
			if not self.dead:
				self.sprite = 0
			self.update_walls()
			self.bird_update()
			self.update_base()
			pygame.display.update()


	def pauseGame(self):
		area_back = pygame.Rect(148, 447, 100, 35)
		area_exit = pygame.Rect(148, 492, 100, 35)
		clock = pygame.time.Clock()
		while True:
			clock.tick(60)
			pygame.display.update()
			self.screen.blit(self.paused, (55, 157))
			self.screen.blit(self.back, (148,447))
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
						if area_back.collidepoint(event.pos):	
							#time.sleep(0.3)
							return 0
						elif area_exit.collidepoint(event.pos):
							self.start_menu()


	def scoreGame(self):
		pygame.font.init()
		font = pygame.font.SysFont("Arial", 35)
		area_back = pygame.Rect(148, 447, 100, 35)
		area_exit = pygame.Rect(148, 492, 100, 35)
		clock = pygame.time.Clock()
		while True:
			clock.tick(60)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if area_back.collidepoint(event.pos):	
							self.start_menu()
			self.screen.fill((255, 255, 255)) 
			self.screen.blit(self.background, (-1, 0))
			self.screen.blit(self.base, (self.baseX, 597))
			self.screen.blit(self.score_message, (106, 60))
			self.screen.blit(self.score_table, (59, 160))
			self.screen.blit(self.back, (148, 447))
			totalScore = self.readFile()
			self.screen.blit(font.render(str(totalScore),	
										 -1,
										 (255, 255, 255)),
										 (267, 248))


if __name__ == "__main__":
	main_window = KlappyBird()
	main_window.start_menu()
    