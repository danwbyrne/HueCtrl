import screenGrab
import tkinter as tk
import numpy as np
import pyhue
import time
import json

def RGBtoHEX(rgb):
	return "#" + ''.join( ['%X' % int(value) for value in rgb])

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.config = None

		self.pack()
		self.loadConfig()
		self.create_widgets()

	def loadConfig(self):

		with open('config.json', 'rb') as cfg_file:
			self.config = json.load(cfg_file)

	def create_widgets(self):
		self.start_button = tk.Button(self)

		self.start_button['text']    = "Click to start HueCtrl"
		self.start_button['command'] = self.run()
		self.start_button.pack(side = "top")

	def getColor(self):
		color  = np.zeros(3)
		screen = screenGrab.getPixels( self.config['monitor'] )
		shape  = screen.shape[:2]
		num    = shape[0]*shape[1]

		for y in range(shape[0]):
			for x in range(shape[1]):

				color = np.add(color, screen[y,x])

		return np.divide(color, num)

	def run(self):
	
		self.start_button.config( bg = RGBtoHEX(self.getColor()) )







def speedTest(monitor):
	return sum([pixelTest(monitor) for i in range(100)])/100.

def pixelTest(monitor):
	start = time.time()
	screenGrab.getPixels(monitor)
	return time.time()-start

def main():
	root = tk.Tk()
	ctrl = Application()
	ctrl.mainloop()

if __name__ == "__main__":
	main()