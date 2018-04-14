import numpy as np
import cv2
import mss

def test():

	with mss.mss() as sct:
		monitor = sct.monitors[1]
		sct_img = sct.grab(monitor)
		#img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
		img  = np.asarray(sct_img)
		print(img)


	