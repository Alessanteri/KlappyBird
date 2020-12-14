import pygame
from pygame.locals import *  # noqa
import sys
import random

from settings import Settings


class Background(Settings):

	def update_walls(self):
		self.wallx -= 2 
		if self.wallx == 80:
			self.counter += 1
		if self.wallx < -80:
			self.wallx = 400
			self.offset = random.randint(-50, 310)


	def update_base(self):
		self.baseX -= 2
		if self.baseX == -398:
			self.baseX = 0




