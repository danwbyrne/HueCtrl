import screenGrab
import numpy as np
import pyhue
import math
import time
import json

def RGBtoHEX(rgb):
	return "#" + ''.join( ['%X' % int(value) for value in rgb])

def RGBtoXY(rgb):
	trans_mat = np.matrix( [[.65, .1035, .197],[.234, .743, .023],[0, .053, 1.036]] )
	norm      = list( map(enhanceColor, np.divide(rgb, 255.)) )
	xyz       = np.dot(trans_mat, np.transpose(norm))
	mag       = np.sum(xyz)

	if mag == 0:
		return (0., 0.)

	return np.divide(xyz[:2], mag)

def enhanceColor(value):

	if value > .0405: return math.pow( (value + .055)/(1.055), 2.4)
	return value / 12.92

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
	
		while True:
			print(RGBtoXY(self.getColor()))






def speedTest(monitor):
	return sum([pixelTest(monitor) for i in range(100)])/100.

def pixelTest(monitor):
	start = time.time()
	screenGrab.getPixels(monitor)
	return time.time()-start






def main():

	ctrl = Application()
	ctrl.mainloop()

if __name__ == "__main__":
	main()