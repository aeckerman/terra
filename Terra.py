from turtle import *

class World:
	'''Class for world in which you can create organisms.'''
	def __init__(self, world, color, width , height):
		self.world = world
		self.width = width
		self.height = height
		self.color = color

	def create(self):
		bgcolor(self.color)
		title(self.world)
		self.world = setup(self.width, self.height)

		return self.world

	def specs(self):
		specs = 'World: %s\nWidth & Height: %s/%s' % (self.world, self.width, self.height)
		return specs

class Organism:
	'''Class for organism that you can control.'''
	def __init__(self, organism, xy, color, size):
		self.organism = organism
		self.xy = xy
		self.color = color
		self.size = size

	def create(self):
		self.organism = Turtle()
		self.organism.setx(self.xy[0])
		self.organism.sety(self.xy[1])
		self.organism.color(self.color)
		self.organism.shape("circle")
		self.organism.shapesize(self.size)
		self.organism.pu()

		return self.organism

	def specs(self):
		specs = 'Organism: %s\nPosition: %s/%s\nSize: %s' % (self.organism, self.xy[0], self.xy[1], self.size)
		return specs

	def setspeed(self, speed):
		self.organism.speed(speed)

	def setcoords(self, xy):
		self.organism.setx(xy[0])
		self.organism.sety(xy[1])



#           __    _ __
# _      __/ /_  (_) /____  _________  ____ _________
#| | /| / / __ \/ / __/ _ \/ ___/ __ \/ __ `/ ___/ _ \
#| |/ |/ / / / / / /_/  __(__  ) /_/ / /_/ / /__/  __/
#|__/|__/_/ /_/_/\__/\___/____/ .___/\__,_/\___/\___/
#                            /_/
