import pygame
import math
WINDOWX    = 500
WINDOWY    = 500

#RABBIT PROPERTIES
TURTLE_WIDTH = 25
TURTLE_HEIGHT = 25
NOSEANGLE  = 15

class Rabbit:

	def __init__(self, mainx, mainy):
		self.x = mainx/2
		self.y = mainy/2
		self.angle = 0
		self.angleRad = 0
		self.pointStart = []
		self.pointEnd = []
		self.lineColor = []
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
		if type(angle) == int:
			self.angle += angle
			self.angleRad = math.radians(self.angle)
			self.image = rot_center(self.imageSave, self.image,self.angle)
		else:
			if (angle == 'lewo'):
				angle = 180
			elif (angle == 'prawo'):
				angle = 0
			elif (angle == 'gora'):
				angle = 90
			elif (angle == 'dol'):
				angle = -90
			self.angle = angle
			self.angleRad = math.radians(self.angle)
			self.image = rot_center(self.imageSave, self.image,self.angle)

	def mvForward(self, distance, screen):
		self.pointStart.append((self.x, self.y))
		self.imageRect = self.imageRect.move([int(distance * math.cos(self.angleRad)), int(-distance * math.sin(self.angleRad))])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
	def home(self):
		self.x = WINDOWX/2
		self.y = WINDOWY/2
		self.angle = 0
		self.angleRad = 0
		self.pointStart = []
		self.pointEnd = []
		self.image = self.imageSave
		self.imageRect = self.imageSave.get_rect()
		self.imageRect = self.imageRect.move([self.x , self.y ])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
	def jump(self, x, y, screen):
		self.x = x
		self.y = y
		self.imageRect = self.imageRect.move([self.x , self.y ])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery

def rot_center(orig_image, image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(orig_image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image