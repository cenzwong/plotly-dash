import cv2

import ipywidgets
from IPython.display import display as ipydisplay

image_widget = ipywidgets.Image(
    format='jpg',
    width=300,
    height=400,
)
prediction_text_widget = ipywidgets.Text(description='Prediction')
ipydisplay(image_widget)
ipydisplay(prediction_text_widget)
prediction_text_widget.value = ""
cap = cv2.VideoCapture('http://172.16.11.10:8080/stream.mjpeg')
# cap = cv2.VideoCapture('http://172.16.11.10:8080/video')
# cap = cv2.VideoCapture('http://172.16.11.10:4747/video')

count_frame = 0
while True:
    ret, frame = cap.read()
    count_frame = count_frame + 1
    cap.set(cv2.CAP_PROP_FPS, 30)
    fps = cap.get(cv2.CAP_PROP_FPS)
#   cv2.imshow('Video', frame)
    
    # JPEG
    _, jpeg_frame = cv2.imencode('.jpg', frame)
    cam_jpeg = jpeg_frame.tobytes()
    
    if count_frame % 100 == 0:
        base64_image = base64.b64encode(cam_jpeg).decode('utf-8')
        payload = "{\"inputs\":{\"Image\":\""+str(base64_image)+"\"}}"
        response = requests.request("POST", url, data=payload)
        
        prediction_text_widget.value = json.loads(response.text)['outputs']['Prediction'][0] + " @ fps: "+  str(fps)
    
    
        
    # update the camera widget
    image_widget.value = cam_jpeg
    if cv2.waitKey(1) == 27:
        exit(0)
