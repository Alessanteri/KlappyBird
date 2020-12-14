import pygame
from pygame.locals import * 
import sys
import random

class Settings:
	def __init__(self):
		self.screen = pygame.display.set_mode((397, 709))
		self.bird = pygame.Rect(65, 50, 50, 50)
		self.backgroundDay = pygame.image.load("F:/TRITPO/Klappy/assets/background-day.png")
		self.backgroundNight = pygame.image.load("F:/TRITPO/Klappy/assets/background-night.png")
		self.base = pygame.image.load("F:/TRITPO/Klappy/assets/base.png")
		self.paused = pygame.image.load("F:/TRITPO/Klappy/assets/paused.png")

		self.yellowBirdSprites = [pygame.image.load("F:/TRITPO/Klappy/assets/yellowbird-upflap.png"),
								  pygame.image.load("F:/TRITPO/Klappy/assets/yellowbird-downflap.png"),
								  pygame.image.load("F:/TRITPO/Klappy/assets/dead.png"),
								  pygame.image.load("F:/TRITPO/Klappy/assets/yellowbird-midflap.png")]
		self.yellowBirdPressed = pygame.image.load("F:/TRITPO/Klappy/assets/yellowBridPress.png")

		self.redBirdSprites = [pygame.image.load("F:/TRITPO/Klappy/assets/redbird-upflap.png"),
							   pygame.image.load("F:/TRITPO/Klappy/assets/redbird-downflap.png"),
							   pygame.image.load("F:/TRITPO/Klappy/assets/dead.png"),
							   pygame.image.load("F:/TRITPO/Klappy/assets/redbird-midflap.png")]
		self.redBirdPressed = pygame.image.load("F:/TRITPO/Klappy/assets/redBirdPress.png")

		self.blueBirdSprites = [pygame.image.load("F:/TRITPO/Klappy/assets/bluebird-upflap.png"),
							   pygame.image.load("F:/TRITPO/Klappy/assets/bluebird-downflap.png"),
							   pygame.image.load("F:/TRITPO/Klappy/assets/dead.png"),
							   pygame.image.load("F:/TRITPO/Klappy/assets/bluebird-midflap.png")]
		self.blueBirdPressed = pygame.image.load("F:/TRITPO/Klappy/assets/blueBirdPress.png")

		self.birdStyle = self.yellowBirdSprites
		self.birdStylePress = self.yellowBirdPressed
		self.redBird = pygame.image.load("F:/TRITPO/Klappy/assets/redBird.png")
		self.yellowBird = pygame.image.load("F:/TRITPO/Klappy/assets/yellowBrid.png")
		self.blueBird = pygame.image.load("F:/TRITPO/Klappy/assets/blueBird.png") 

		# self.numberOfScore = [pygame.image.load("F:/TRITPO/assets/0.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/1.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/2.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/3.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/4.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/5.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/6.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/7.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/8.png"),
		# 					  pygame.image.load("F:/TRITPO/assets/9.png")]

		self.message = pygame.image.load("F:/TRITPO/Klappy/assets/message.png ")
		self.menu = pygame.image.load("F:/TRITPO/Klappy/assets/menu.png")
		self.start = pygame.image.load("F:/TRITPO/Klappy/assets/start.png")
		self.style = pygame.image.load("F:/TRITPO/Klappy/assets/style.png")
		self.score = pygame.image.load("F:/TRITPO/Klappy/assets/score.png")
		self.score_table = pygame.image.load("F:/TRITPO/Klappy/assets/score_table.png")
		self.score_message = pygame.image.load("F:/TRITPO/Klappy/assets/score_message.png")
		self.exit = pygame.image.load("F:/TRITPO/Klappy/assets/exit.png")
		self.back = pygame.image.load("F:/TRITPO/Klappy/assets/back.png")

		self.pipe_green = pygame.image.load("F:/TRITPO/Klappy/assets/pipe_green.png")
		self.bd = pygame.image.load("F:/TRITPO/Klappy/assets/bd.png")


		self.wallUp = pygame.image.load("F:/TRITPO/Klappy/assets/pipe-green-buttom.png")
		self.wallDown = pygame.image.load("F:/TRITPO/Klappy/assets/pipe-green-top.png")
		self.table = pygame.image.load("F:/TRITPO/Klappy/assets/table.png")
		self.day = pygame.image.load("F:/TRITPO/Klappy/assets/day.png")
		self.dayPress = pygame.image.load("F:/TRITPO/Klappy/assets/dayPress.png")
		self.night = pygame.image.load("F:/TRITPO/Klappy/assets/night.png")
		self.nightPress = pygame.image.load("F:/TRITPO/Klappy/assets/nightPress.png")

		self.background = self.backgroundDay
		self.gap = 130
		self.wallx = 400
		self.birdY = 350
		self.jump = 0
		self.jumpSpeed = 20
		self.gravity = 5
		self.dead = False
		self.sprite = 0
		self.counter = 0
		self.counterCounter = 0
		self.offset = random.randint(-50, 310)
		self.pause = False
		self.baseX = 0 
		self.imageX = -40


	def score(self, counter):
		#lenCounter = len(counter)
		numberScore = []
		counterStr = str(counter)
		for i in range(len(str(counter))):
			print(len(str(counter)))
			numberScore.append(int(counterStr[i]))
		return numberScore


	def readFile(self):
		f = open("F:/TRITPO/Klappy/score.txt", "r")
		score = int(f.readline())
		f.close()
		return score


	def writeFile(self, counter):
		if counter > self.readFile():
			f = open("F:/TRITPO/Klappy/score.txt", 'w')
			f.write(str(counter))
			f.close()