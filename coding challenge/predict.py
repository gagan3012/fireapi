
	try:
		prediction = model.predict(data)
	except :
		prediction = None

	return prediction
