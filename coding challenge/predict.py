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
