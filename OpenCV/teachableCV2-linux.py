# wget https://github.com/helloezmeral/what-is-this-local/blob/main/keras_model.h5?raw=true -O keras_model.h5
# wget https://github.com/helloezmeral/what-is-this-local/blob/main/labels.txt?raw=true -O labels.txt

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
label_file = "./labels.txt"
labels = []
with open(label_file, "r") as f:
        labels = [line.strip().split(' ',1) for line in f]
print(model)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def jpgResize(image, w, h):
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (w, h)
    return ImageOps.fit(image, size, Image.ANTIALIAS)

def run_prediction(in_image_array):

    # Normalize the image
    normalized_image_array = (in_image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return prediction, labels[np.argmax(prediction[0])]

import cv2
import time

cap = cv2.VideoCapture('http://172.16.11.10:8080/stream.mjpeg')
# cap = cv2.VideoCapture('http://172.16.11.10:8080/video')
# cap = cv2.VideoCapture('http://172.16.11.10:4747/video')

thisTime = time.time()
cvText = ""
while True:
    ret, frame = cap.read()
    cap.set(cv2.CAP_PROP_FPS, 30)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)  
    cv2.resizeWindow("Video", 720, 720)  
    cv2.putText(frame, cvText, (0, 100), cv2.FONT_HERSHEY_PLAIN, 5.5, (0,255,0), 5) # must be on top of imshow
    cv2.imshow('Video', frame)

    # JPEG
    image = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    image = jpgResize(image, 224, 224)
    
    # Drop some of the framerate
    if time.time() - thisTime > 1:
        thisTime = time.time()
        prediction , label = run_prediction(np.asarray(image))
        print("Prediction: ", label[1])
        cvText = label[1]
    
    # update the camera widget
    if cv2.waitKey(1) == 27:
        exit(0)