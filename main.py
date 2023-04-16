import pygame
import sys
from rabbit import Rabbit
import time
import re
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
numerical = "-1234567890,*/+-=><!"
boolean = ['bool']
DECLARATIONS = ['int', 'bool', 'fun']
mathematical = ['+', '-', '*', '/']
whitespace_key = "\t \r \n"
eof_key = '\0'
BOOLEAN = "Boolean"
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
dec = {}
class Token:
	def __init__(self, startChar):
		self.value = startChar
		self.type = None
class Tokenizer:
	def __init__(self,source):
		self.scanner = Scanner(source)
		self.lista = []
	def calculate(self, split_string):
		split_string = re.split(r'([*/+-])', split_string)
		print(split_string)
		for v in split_string:
			if v in ['*', '/']:
				operator = split_string.index(v)
				dsa = dec[split_string[operator - 1]] if split_string[operator - 1] in dec else split_string[operator - 1]
				dsa2 = dec[split_string[operator + 1]] if split_string[operator + 1] in dec else split_string[operator + 1]
				v1 = operator - 1
				v2 = operator + 1
				if v == '*':
					split_string[v1] = str(int(dsa) * int(dsa2))
					split_string.pop(v2)
					split_string.pop(operator)
				elif v == '/':
					split_string[v1] = str(int(int(dsa) / int(dsa2)))
					split_string.pop(v2)
					split_string.pop(operator)
		while len(split_string) > 1:
			for v in split_string:
				if v in ['+', '-']:
					operator = split_string.index(v)
					dsa = dec[split_string[operator - 1]] if split_string[operator - 1] in dec else split_string[
						operator - 1]
					dsa2 = dec[split_string[operator + 1]] if split_string[operator + 1] in dec else split_string[
						operator + 1]
					v1 = operator - 1
					v2 = operator + 1
					if v == '+':
						split_string[v1] = str(int(dsa) + int(dsa2))
						split_string.pop(v2)
						split_string.pop(operator)
					elif v == '-':
						split_string[v1] = str(int(dsa) - int(dsa2))
						split_string.pop(v2)
						split_string.pop(operator)
		return split_string[0]
	def compare(self,list):
		split_string = re.split(r'(\s*(?:)!=|>=|<=|==|[<>])', list)
		v1 = self.calculate(split_string[0])
		v2 = self.calculate(split_string[2])
		com = split_string[1]
		if com == '==':
			if v1 == v2:
				return True
		elif com == '!=':
			if v1 != v2:
				return True
		elif com == '>':
			if v1 > v2:
				return True
		elif com == '<':
			if v1 < v2:
				return True
		elif com == '>=':
			if v1 >= v2:
				return True
		elif com == '<=':
			if v1 <= v2:
				return True
		return False
	def logicalCompare(self):
		while len(self.lista) > 3:
			for v in self.lista:
				if v == 'and':
					operator = self.lista.index(v)
					v1 = self.lista[operator - 1]
					if v1 in dec.keys():
						v1 = dec[v1]
					if v1 not in ['True', 'False', 'true', 'false']:
						v1 = self.compare(self.lista[operator - 1])
					v2 = self.lista[operator + 1]
					if v2 in dec.keys():
						v2 = dec[v2]
					if v2 not in ['True', 'False', 'true', 'false']:
						v2 = self.compare(self.lista[operator + 1])
					self.lista[operator - 1] = str(v1 and v2)
					self.lista.pop(operator + 1)
					self.lista.pop(operator)
				elif v == 'or':
					operator = self.lista.index(v)
					v1 = self.lista[operator - 1]
					if v1 not in ['True', 'False', 'true', 'false']:
						v1 = self.compare(self.lista[operator - 1])
					v2 = self.lista[operator + 1]
					if v2 not in ['True', 'False', 'true', 'false']:
						v2 = self.compare(self.lista[operator + 1])
					value = True if v1 == True or v2 == True else False
					self.lista[operator - 1] = str(value)
					self.lista.pop(operator + 1)
					self.lista.pop(operator)
		return self.lista[2]
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
			if len(self.lista) > 3:
				if self.lista[1] not in dec.keys():
					dec[self.lista[1]] = self.logicalCompare()
				else:
					print("Variable already declared or wrong value")
			return token
		if char in alphabetical:
			token.type = IDENTIFIER
			char = self.getChar()
			while char in alphabetical + numerical:
				token.value += char
				char = self.getChar()
			if token.value in keywords:
				token.type = KEYWORD
			if token.value in DECLARATIONS:
				token.type = 'Declaration'
			if 'bool' in self.lista or token.type == 'Declaration' or 'int' in self.lista or 'fun' in self.lista:
				self.lista.append(token.value)
			if len(self.lista) == 3:
				if self.lista[1] not in dec.keys() and self.lista[2] in ['True', 'False', 'true', 'false']:
					dec[self.lista[1]] = self.lista[2]
				else:
					print("Variable already declared or wrong value", self.lista)
			return token
		if char in numerical or alphabetical:
			token.type = NUMERIC
			char = self.getChar()
			while char in numerical or char in alphabetical:
				token.value += char
				char = self.getChar()
			vas = (token.value.find('>') or token.value.find('<') or token.value.find('==') or token.value.find('!='))
			#print(token.value)
			if vas != -1:
				self.lista.append(token.value)
			else:
				self.lista.append(token.value)
				if len(self.lista) > 2 and self.lista[1] not in dec.keys():
					dec[self.lista[1]] = self.calculate(self.lista[2])
				token.value = self.calculate(token.value)
			#print(token.value)
			return token

	def getChar(self):
		char = self.scanner.scan()
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
			self.index = self.index + 1
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
		if nextToken == "":
			return
		if nextToken.type == 'Declaration':
			return
		if nextToken.value not in keywords:
			print("Niezgodnosc z gramatyka: " + nextToken.value)
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
				print("Niepoprawny kierunek")
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
with open("test.rabbit", "r") as f:
	for line in f:
		time.sleep(0.1)
		if line != "\n":
			source = line
			print(dec)
			P.reInit(source)
			P.parse()



while True:
	source = input()
	if source == "exit":
		break
	source = source + "  "
	P.reInit(source)
	P.parse()
