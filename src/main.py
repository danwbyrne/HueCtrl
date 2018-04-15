import screenGrab
import pyhue
import time
import json

class App():

	def __init__(self):

		self.config = None




		loadConfig()

	def loadConfig(self):

		with open('config.json', 'rb') as cfg_file:
			self.config = json.load(cfg_file)

	def test(self):

		return speedTest(self.config['monitor'])


def speedTest(monitor):

	return sum([pixelTest(monitor) for i in range(100)])/100.

def pixelTest(monitor):
	start = time.time()
	screenGrab.getPixels(monitor)
	return time.time()-start

def main():
	ctrl = App()
	print(ctrl.test())

if __name__ == "__main__":
	main()