import tensorflow as tf
from tensorflow.keras.preprocessing import image as tf_keras_preprocessing_image
import time
import numpy as np

def keras_model(keras_appl_model_obj, keras_appl_model, image_path, target_size):

  nowtime = time.time()

  model = keras_appl_model_obj(weights='imagenet')

  img_path = image_path
  img = tf_keras_preprocessing_image.load_img(img_path, target_size=target_size)
  x = tf_keras_preprocessing_image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = keras_appl_model.preprocess_input(x)

  preds = model.predict(x)
  
  print(keras_appl_model_obj.__name__," takes ", time.time() - nowtime, " to run")
  print('Predicted:', keras_appl_model.decode_predictions(preds, top=3)[0])
  print('====')
  

  
# Run the model
from tensorflow.keras.applications import resnet50, vgg16, inception_v3, densenet, efficientnet, mobilenet_v2

image_path = 'images/1.png'

keras_model(resnet50.ResNet50, resnet50, image_path, (224, 224))
keras_model(vgg16.VGG16, vgg16, image_path, (224, 224))
keras_model(inception_v3.InceptionV3, inception_v3, image_path, (299, 299))
keras_model(densenet.DenseNet121, densenet, image_path, (224, 224))
keras_model(efficientnet.EfficientNetB2, efficientnet, image_path, (260, 260))
keras_model(mobilenet_v2.MobileNetV2, mobilenet_v2, image_path, (224, 224))










