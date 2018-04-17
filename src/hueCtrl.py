import screenGrab
import numpy as np
import threading
import pyhue
import time
import json

class Application(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.config  = None
		self.bridge  = None
		self.capture = None

		self.loadConfig()
		self.connect()

	def loadConfig(self):

		with open('config.json', 'rb') as cfg_file:
			self.config = json.load(cfg_file)

	def loadCapture(self, capture):
		self.capture = capture

	def connect(self):
		self.bridge = pyhue.Bridge(self.config['bridge'], self.config['username'])
		on_state = json.dumps({"on":True, "bri":255})
		for light_id in self.config['lights']:
			self.bridge.setState(light_id, on_state)

	def run(self):
	
		print("Running")
		while True:
			
			new_color = self.capture.getValue()
			new_xy    = pyhue.RGBtoXY(new_color[0], new_color[1], new_color[2])
			new_bri   = pyhue.getBri(new_color)

			temp_state = json.dumps({"xy":new_xy, "bri":new_bri, "transitiontime":0})
			self.bridge.setState(21, temp_state)

			time.sleep(.15) #sleep so we can limit our commands/sec to around 10/sec