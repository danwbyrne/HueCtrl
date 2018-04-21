import numpy as np
import threading
import mss


#taken from http://python-mss.readthedocs.io/examples.html#fps BGRA to RGB numpy method
def getRGB(im):
    
    frame = np.array(im, dtype=np.uint8)
    return np.flip(frame[:, :, :3], 2)

class Capture(threading.Thread):

	def __init__(self, monitor):
		threading.Thread.__init__(self)

		self.monitor = monitor
		self.cptr    = np.asarray([[0,0,0]])
		self.value   = self.getColor()

	def grab(self):

		with mss.mss() as capture:
			self.cptr = np.array( getRGB( capture.grab(self.monitor) ) )

	def getColor(self):

		color  = np.zeros(3)
		screen = self.cptr
		shape  = screen.shape[:2]
		num    = shape[0]*shape[1]

		for y in range(shape[0]):
			for x in range(shape[1]):

				color = np.add(color, screen[y,x])

		rgb = np.divide(color, num*255.)
		return rgb

	def run(self):

		try:

			while True:
				
				self.grab()
				self.value = self.getColor()

		except KeyboardInterrupt:
			exit()

	def getValue(self):

		return self.value

	