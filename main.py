import pygame
import sys
from rabbit import Rabbit
keywords = """
go
angle
home
jump
reset
getX
getY
setView
"""
keywords= keywords.split()
alphabetical = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerical = "-1234567890,"
whitespace_key = "\t \r \n"
eof_key = '\0'
IDENTIFIER = "Indentifier"
KEYWORD = "Keyword"
WHITESPACE = "Whitespace"
NUMERIC = "Numeric"
OPERATOR = "Operator"
EOF = 'Eof'
WINDOWX    = 500
WINDOWY    = 500
RABBIT_WIDTH = 25
RABBIT_HEIGHT = 25
NOSEANGLE = 15
class Token:
	def __init__(self, startChar):
		self.value = startChar
		self.type = None
class Tokenizer:
	def __init__(self,source):
		self.scanner = Scanner(source)
	def getToken(self):
		char = self.getChar()
		if char in " \t \n":
			char = self.getChar()
			while char in " \t \n":
				char = self.getChar()
			return None
		token = Token(char)
		if char in eof_key:
			token.type = EOF
			return token
		if char in alphabetical:
			token.type = IDENTIFIER
			char = self.getChar()
			while char in alphabetical + numerical:
				token.value += char
				char = self.getChar()
			if token.value in keywords:
				token.type = KEYWORD
			return token
		if char in numerical:
			token.type = NUMERIC
			char = self.getChar()
			while char in numerical:
				token.value += char
				char = self.getChar()
			return token
	def getChar(self):
		char   = self.scanner.scan()
		return char
class Scanner:
	def __init__(self, source):
		self.source = source
		try:
			self.file = self.source
			self.eof = len(self.file) - 1
			self.index = 0
		except Exception as e:
			raise e
	def scan(self):
		if self.index < self.eof:
			char = self.file[self.index]
			self.index = self.index +  1
			return char
		return '\0'
class Parser:
	def __init__(self, source):
		self.T = Tokenizer(source)
		self.tokenList = []
		self.createTokenList()
		self.index = -1
	def reInit(self, source):
		self.T = Tokenizer(source)
		self.tokenList = []
		self.createTokenList()
		self.index = -1
	def createTokenList(self):
		while True:
			token = self.T.getToken()
			if token is  not None:
				self.tokenList.append(token)
				if token.type == EOF:
					break
	def lookNextToken(self):
		try:
			return self.tokenList[self.index + 1]
		except IndexError as e:
			return None
	def currToken(self):
		return self.tokenList[self.index]
	def getNextToken(self):
		self.index += 1
		return self.tokenList[self.index]
	def graphInit(self):
		pygame.init()
		self.white = 255, 255 , 255
		self.screen = pygame.display.set_mode((WINDOWX,WINDOWY))
		self.Rabbit = Rabbit(WINDOWX, WINDOWY)
		self.Rabbit.setImage(pygame.image.load("rabbit.png"))
		self.screen.fill(self.white)
		self.Rabbit.draw(self.screen)
		pygame.display.flip()
		pygame.display.set_icon(pygame.image.load("rabbit.png"))
		pygame.display.set_caption("Rabbit")
	def parse(self):
		self.parseSentence()
		while True:
			tokenAhead = self.lookNextToken()
			if tokenAhead == None:
				break
			elif tokenAhead.type == EOF:
				break
			elif tokenAhead.type == KEYWORD:
				self.parseSentence()
			else:
				break
	def parseSentence(self):
		nextToken = self.lookNextToken()
		if nextToken.value not in keywords:
			print("Niezgodnosc z gramatyka")
			return
		if nextToken.value in ['go']:
			self.Match()
			if(self.Match(NUMERIC) == -1):
				return
			self.Rabbit.mvForward(int(self.currToken().value), self.screen)
		if nextToken.value in ['angle']:
			self.Match()
			if(self.Match(NUMERIC) == -1):
				return
			katy = [0, 90, 180, 270, 360]
			if int(self.currToken().value) not in katy:
				print("Niepoprawny kat")
				return
			self.Rabbit.rotate(int(self.currToken().value))
			print(self.currToken().value)
		if nextToken.value in ['home']:
			self.Match()
			self.Rabbit.home()
		if nextToken.value in ['jump']:
			self.Match()
			if (self.Match(NUMERIC) == -1):
				return
			tab = self.currToken().value.split(",")
			if len(tab) != 2:
				print("Niepoprawna liczba argumentow")
				return
			self.Rabbit.jump(int(tab[0]), int(tab[1]), self.screen)
		if nextToken.value in ['reset']:
			self.Match()
			P.graphInit()
		# if nextToken.value in ['getX']:
		# 	self.Match()
		# 	self.Rabbit.getX()
		# if nextToken.value in ['getY']:
		# 	self.Match()
		# 	self.Rabbit.getY()
		if nextToken.value in ['setView']:
			self.Match()
			if (self.Match(IDENTIFIER) == -1):
				return
			katy = ["prawo","gora","dol","lewo"]
			if self.currToken().value not in katy:
				print("Niepoprawny kat")
				return
			self.Rabbit.rotate(self.currToken().value)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		self.screen.fill(self.white)
		self.Rabbit.draw(self.screen)
		pygame.display.flip()
	def Match(self, expectedTokenType = None):
		token = self.getNextToken()
		if(expectedTokenType == None):
			return
		if(token.type != expectedTokenType):
			print("Expected token type " + expectedTokenType + " but got " + token.type)
			return -1
print("Podaj komendy: ")
source = " "
P = Parser(source)
P.graphInit()

while True:
	source = input()
	if source == "exit":
		break
	source = source + "  "
	P.reInit(source)
	P.parse()