import numpy as np
import mss
import cv2

#taken from http://python-mss.readthedocs.io/examples.html#fps BGRA to RGB numpy method
def getRGB(im):
    
    frame = np.array(im, dtype=np.uint8)
    return np.flip(frame[:, :, :3], 2)

def getPixels():

	#mon = {'top': 40, 'left': 0, 'width': 800, 'height': 640}

	with mss.mss() as sct:
		monitor = sct.monitors[1]
		img  = np.array(getRGB(sct.grab(monitor)))