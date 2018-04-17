import hueCtrl
import screenGrab
import threading

def main():
	
	threads = []
	ctrl = hueCtrl.Application()
	our_capture = screenGrab.Capture(ctrl.config['monitor'])
	ctrl.daemon = True
	our_capture.daemon = True
	ctrl.loadCapture(our_capture)
	our_capture.start()
	ctrl.start()
	threads.append(our_capture)
	threads.append(ctrl)

	for t in threads:
		t.join()


if __name__ == "__main__":
	main()