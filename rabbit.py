import math

import pygame

WINDOWX    = 500
WINDOWY    = 500

RABBIT_WIDTH = 25
RABBIT_HEIGHT = 25
NOSEANGLE  = 15

class Rabbit:

	def __init__(self,mainx,mainy):
		self.x = mainx/2
		self.y = mainy/2
		self.angle = 0
		self.angleRad = 0
		self.pointStart = []
		self.pointEnd = []

	def draw(self, screen):
		screen.blit(self.image, self.imageRect)

	def setImage(self, image):
		self.image = image
		self.imageSave = self.image
		self.imageRect = image.get_rect()
		self.imageRect = self.imageRect.move([self.x , self.y ])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery

	def rotate(self, angle):
		if(angle == 'lewo'):
			angle = 180
		elif(angle == 'prawo'):
			angle = 0
		elif(angle == 'gora'):
			angle = 90
		elif(angle == 'dol'):
			angle = -90
		self.angle = angle
		self.angleRad = math.radians(self.angle)

	def mvForward(self, distance, screen):
		self.imageRect = self.imageRect.move([int(distance * math.cos(self.angleRad)), int(-distance * math.sin(self.angleRad))])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery

