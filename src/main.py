import screenGrab
import pyhue
import time

def main():
	start = time.time()
	screenGrab.test()
	print('time for test: %.5f secs' % (time.time() - start))

if __name__ == "__main__":
	main()