import screenGrab
import numpy as np
import pyhue
import math
import time
import json

def enhanceColor(value):
	if value > 0.04045:
		return math.pow( (value + .055)/(1.055), 2.4)
	return value / 12.92
		
def RGBtoXY(rgb):
	norm = list(map(enhanceColor, rgb))
	trans_mat = np.matrix([[.65, .1035, .197], [.234, .743, .023], [0., .053, 1.036]])
	xyz = np.dot(trans_mat, norm)
	mag = np.sum(xyz)

	if mag == 0:
		return (0,0)

	return xyz[0]

def getBri(rgb):
	return int((0.299*rgb[0] + 0.587*rgb[1] + 0.0722*rgb[2])*255.)

class Application():

	def __init__(self):
		self.config = None
		self.bridge = None

		self.loadConfig()
		self.connect()

	def loadConfig(self):

		with open('config.json', 'rb') as cfg_file:
			self.config = json.load(cfg_file)

	def connect(self):
		self.bridge = pyhue.Bridge(self.config['bridge'], self.config['username'])
		on_state = json.dumps({"on":True, "bri":255})
		for light_id in self.config['lights']:
			self.bridge.setState(light_id, on_state)

	def getColor(self):
		color  = np.zeros(3)
		screen = screenGrab.getPixels( self.config['monitor'] )
		shape  = screen.shape[:2]
		num    = shape[0]*shape[1]

		for y in range(shape[0]):
			for x in range(shape[1]):

				color = np.add(color, screen[y,x])

		rgb = np.divide(color, num*255.)
		return rgb

	def mainloop(self):
	
		while True:
			#start = time.time()
			new_color = self.getColor()
			new_xy    = pyhue.rgb2xy(new_color[0], new_color[1], new_color[2])
			new_bri   = getBri(new_color)

			temp_state = json.dumps({"xy":new_xy, "bri":new_bri, "transitiontime":0})
			self.bridge.setState(21, temp_state)
			#end = time.time()

			#sleep_diff = (end-start)
			#if sleep_diff < .1:
			time.sleep(.1) #sleep so we can limit our commands/sec to around 10/sec



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