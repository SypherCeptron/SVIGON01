
from imutils.video import VideoStream
from pyimagesearch.blur_detector import detect_blur_fft
import imutils
from time import time
import time as tx
import cv2
def BFT():

# initialize the video stream and allow the camera sensor to warm up
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	tx.sleep(2.0)
	Start = time()
	Maxmean = 0
	frame = vs.read()
	framex = imutils.resize(frame, width=500)
# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=500)

		# convert the frame to grayscale and detect blur in it
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		(mean, blurry) = detect_blur_fft(gray)
		if	Maxmean<=mean:
			Maxmean =mean
			framex =frame


		# show the output frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

		# do a bit of cleanup



		if blurry == False:
			cv2.destroyAllWindows()
			vs.stop()

			return frame
		stop =time()
		if int(stop - Start) >5:
			cv2.destroyAllWindows()
			vs.stop()

			return framex
