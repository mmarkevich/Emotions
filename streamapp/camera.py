import numpy as np
import cv2, os, urllib.request
from django.conf import settings
from keras.models import model_from_json
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from DB.models import DataAboutUserAndVideo
import time

model = model_from_json(open(r"/Users/andreimarkevich/PycharmProjects/FallbackOptionforFER/streamapp/fer2013_model6.json", "r").read())
model.load_weights(r'/Users/andreimarkevich/PycharmProjects/FallbackOptionforFER/streamapp/fer2013_model6.h5')

face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))

emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

class VideoCamera(object):

	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, cap_img = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		sec=0
		gray = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(cap_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
			cropped_image = gray[y:y + w, x:x + h]
			cropped_image = cv2.resize(cropped_image, (48, 48))
			image_pixels = image.img_to_array(cropped_image)
			image_pixels = np.expand_dims(image_pixels, axis=0)
			image_pixels /= 255

			predictions = model.predict(image_pixels)

			res = np.argmax(predictions[0])


			predicted_emotion = emotions[res]

			cv2.putText(cap_img, predicted_emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 0, 0), 3,cv2.LINE_AA)
#		frame_flip = cv2.flip(cap_img, 1)
		ret, jpeg = cv2.imencode('.jpg', cap_img)

		return jpeg.tobytes()


	def throwData(self):
		a = DataAboutUserAndVideo(ID_user=2, ID_video_information=3,
								  dominant_emotion=predicted_emotion, edited_dominant_emotion=predicted_emotion)
		a.save()