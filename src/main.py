import hueCtrl
import screenGrab
import threading
import time

def main():
	threads = []
	ctrl = hueCtrl.Application()
	our_capture = screenGrab.Capture(ctrl.config['monitor'])
	ctrl.daemon = True
	our_capture.daemon = True
	ctrl.loadCapture(our_capture)
	our_capture.start()
	ctrl.start()
	ctrl.run()

if __name__ == "__main__":
	try:
		main()

	except KeyboardInterrupt:
		exit()