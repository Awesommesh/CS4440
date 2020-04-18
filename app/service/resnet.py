import numpy as np
import tensorflow as tf
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
graph = tf.get_default_graph()


def model_predict(img_path):

	model = ResNet50(weights='imagenet')

	original = image.load_img(img_path, target_size=(224, 224))

	numpy_image = image.img_to_array(original)
	
	image_batch = np.expand_dims(numpy_image, axis=0)

	processed_image = preprocess_input(image_batch, mode='caffe')


	with graph.as_default():
		preds = model.predict(processed_image)

	print('Predicted:', decode_predictions(preds, top=1)[0])

	return preds

if __name__ == '__main__':
	path = 'gorilla.jpg'

	model_predict(path )