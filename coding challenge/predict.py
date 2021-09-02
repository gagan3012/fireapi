# Step 1 - ML in Python coding quiz

# This script is meant to load a serialized model file and return a prediction
# The model can be in Tensorflow or scikit-learn (choose one)
# The model format can be any serialized file format that is appropriate for ML framework that you choose (choose one)

# Please complete the prediction script below (refer to sections marked "TO DO" for parts to be completed)

import sys
from flask import Flask
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

	model = tf.keras.models.load_model(modelfile)
