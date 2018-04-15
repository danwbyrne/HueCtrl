import screenGrab
import numpy as np
import pyhue
import time
import json

def RGBtoHEX(rgb):
	return "#" + ''.join( ['%X' % int(value) for value in rgb])

class Application():

	def __init__(self):
		self.config = None

		self.loadConfig()

	def loadConfig(self):

		with open('config.json', 'rb') as cfg_file:
			self.config = json.load(cfg_file)

	def getColor(self):
		color  = np.zeros(3)
		screen = screenGrab.getPixels( self.config['monitor'] )
		shape  = screen.shape[:2]
		num    = shape[0]*shape[1]

		for y in range(shape[0]):
			for x in range(shape[1]):

				color = np.add(color, screen[y,x])

		return np.divide(color, num)

	def mainloop(self):
	
		pass






def speedTest(monitor):
	return sum([pixelTest(monitor) for i in range(100)])/100.

def pixelTest(monitor):
	start = time.time()
	screenGrab.getPixels(monitor)
	return time.time()-start






def main():

	ctrl = Application()

if __name__ == "__main__":
	main()