"""
Created on Tues Sep 21 12:40:00 2021

@author: Luis Esteban Fortanel Hernandez
"""
from config import (
	current_app, request, jsonify)
from . import distance
from .Controller import calculateDistance

#Setting up the url of the endpoint
@distance.route('/calculateDistance', methods = ["GET"])
def getDistance():
	#The latitude and longitude are obtained from the query params to convert them to float for the operations, if there is an error, a 400 will be returned
	try :
		latPoint = float(request.args.get("lat"))
		longPoint = float(request.args.get("long"))
	except Exception as error:
		return jsonify({"msg": "Invalid Lat or Long value"}), 400

	#The function to calculate the distance between coordinates is called. 
	#I did this so as not to crowd the code into a single file and have better control.
	info_dict, status_code = calculateDistance(latPoint, longPoint)

	#If the answer is correct, it is sent, if not, a 500 is sent
	if info_dict :
		if status_code == 200 :
			#The distance between the coordinates is saved in the .log file
			current_app.logger.info("Miles: " + str(info_dict["result"]["miles"]) + ", " + "KM: " + str(info_dict["result"]["km"]))
		elif status_code == 40 :
			current_app.logger.info("Address is located inside the MKAD")

		return jsonify(info_dict), status_code

	current_app.logger.error(status_code)
	return jsonify({"msg": "Internal Server Error"}),500
