import pygame
import math

class Rabbit:

	def start(self):
		self.white = 255, 255, 255
		self.screen = pygame.display.set_mode((WINDOWX, WINDOWY))
		self.clock = pygame.time.Clock()  # get a pygame clock object
		self.player = self.setImage(pygame.image.load('rabbit.png').convert())
		self.screen.fill(self.white)
		self.draw()

	def __init__(self):
		self.screen = None
		self.clock = None
		self.player = None
		self.position = None
		self.x = WINDOWX/2
		self.y = WINDOWY/2
		self.angle = 0
		self.angleRad = 0
		self.pointStart = []
		self.pointEnd = []
		self.lineColor = []
		self.WINDOWX = WINDOWX
		self.WINDOWY = WINDOWY
	def draw(self):
		self.screen.fill(self.white)
		self.screen.blit(self.image, self.imageRect)
	def setImage(self, image):
		self.image = image
		self.imageSave = self.image
		self.imageRect = self.image.get_rect()
		self.imageRect = self.imageRect.move([self.x , self.y ])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery

	def rotate(self, angle):
		if type(angle) == int:
			self.angle += angle
			self.angleRad = math.radians(self.angle)
			self.image = rot_center(self.imageSave, self.image,self.angle)
			self.draw()
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
			self.draw()
		pygame.display.update()

	def mvForward(self, distance):
		self.pointStart.append((self.x, self.y))
		self.imageRect = self.imageRect.move(
			[int(distance * math.cos(self.angleRad)), int(-distance * math.sin(self.angleRad))])
		self.draw()
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
		pygame.display.update()

	def home(self):
		self.x = self.WINDOWX/2
		self.y = self.WINDOWY/2
		self.angle = 0
		self.angleRad = 0
		self.pointStart = []
		self.pointEnd = []
		self.image = self.imageSave
		self.imageRect = self.imageSave.get_rect()
		self.imageRect = self.imageRect.move([self.x , self.y ])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
		self.draw()
		pygame.display.update()

	def jump(self, x, y):
		self.x = x
		self.y = y
		self.imageRect = self.imageRect.move([self.x, self.y])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
		self.draw()
		pygame.display.update()

def rot_center(orig_image, image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(orig_image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image