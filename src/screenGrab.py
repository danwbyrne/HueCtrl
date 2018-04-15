import numpy as np
import mss



#taken from http://python-mss.readthedocs.io/examples.html#fps BGRA to RGB numpy method
def getRGB(im):
    
    frame = np.array(im, dtype=np.uint8)
    return np.flip(frame[:, :, :3], 2)

def getPixels(monitor):

	with mss.mss() as capture:
		return np.array( getRGB( capture.grab(monitor) ) )