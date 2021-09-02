	#	-load model file
	#	-get prediction
	#	-check for errors

	model = tf.keras.models.load_model(modelfile)

	try:
		prediction = model.predict(data)
	except :
		prediction = None

	return prediction
