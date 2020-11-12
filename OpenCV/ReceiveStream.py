import cv2

# HTTP Stream by Dmitriy Krivoruchko
# cap = cv2.VideoCapture('http://172.16.11.10:8080/stream.mjpeg')

# IP Webcam by Pavel Khlebovich
# cap = cv2.VideoCapture('http://172.16.11.10:8080/video')

# DroidCam by Dev47Apps
cap = cv2.VideoCapture('http://172.16.11.10:4747/video')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  if cv2.waitKey(1) == 27:
    exit(0)
