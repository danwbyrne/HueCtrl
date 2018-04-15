import screenGrab
import pyhue
import time

def speedTest(monitor):

	return sum([test(monitor) for i in range(100)])/100.

def test(monitor):
	start = time.time()
	screenGrab.getPixels(monitor)
	return time.time()-start

def main():
	mon = {"top": 0, "left": 0, "width": 1920, "height": 1080}
	print(speedTest(mon))

if __name__ == "__main__":
	main()