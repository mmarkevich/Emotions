import numpy as np
import cv2
from keras.models import model_from_json
from keras.preprocessing import image


#fer2013_model6 must be substituted with a different name if you want to use a different model
model = model_from_json(open("fer2013_model6.json", "r").read())
model.load_weights('fer2013_model6.h5')


face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

while True:
    ret, captured_image = cap.read()

    gray_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)

    faces = face_haar_cascade.detectMultiScale(gray_image, 1.32, 5)


    for (x, y, w, h) in faces:

        cv2.rectangle(captured_image, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
        cropped_image = gray_image[y:y + w, x:x + h]
        cropped_image = cv2.resize(cropped_image, (48, 48))
        image_pixels = image.img_to_array(cropped_image)
        image_pixels = np.expand_dims(image_pixels, axis = 0)
        image_pixels /= 255

        predictions = model.predict(image_pixels)


        res = np.argmax(predictions[0])

        predicted_emotion = emotions[res]

        cv2.putText(captured_image, predicted_emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 0, 0), 3, cv2.LINE_AA)

    resized_image = cv2.resize(captured_image, (1000, 700))
    cv2.imshow('Application for facial emotion recognition', resized_image)



    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows