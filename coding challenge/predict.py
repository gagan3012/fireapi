import google.cloud.storage as gcs
from flask import request
import os
from flask import jsonify
import tensorflow as tf

# TO DO: Import missing modules/packages (if any)
# Prediction type is not known
# Load the model predict and check for errors

def predict():
	data = request.json
	modelfile = [x for x in os.listdir('.') if 'model' in x][0]

	# TO DO:
	#	-load model file
	#	-get prediction
	#	-check for errors

	model = tf.keras.models.load_model(modelfile)

	try:
		prediction = model.predict(data)
	except :
		prediction = None

	return prediction
