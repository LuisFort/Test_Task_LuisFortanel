"""
Created on Tues Sep 21 12:40:00 2021

@author: Luis Esteban Fortanel Hernandez
"""
from config import ( 
	mkad_km, latMRR, longMRR,
	geodesic)

"""
***********************************************************************
Calculate Distance
***********************************************************************
Description:
    The function calculates the distance between 
    the points of the Moscow Ring Road (latMRR, longMRR) 
    and the address sent by the user (latPoint, longPoint).

Requirements: 
    latPoint: The latitude of the address sent by the user
    longPoint: The longitude of the address sent by the user
    
Return:
    A response object from flask. A dictionary with the 
    answer and a status code.

***********************************************************************
"""
def calculateDistance(latPoint, longPoint):
	#It tries to do the operations, if there is an unexpected error, a false is sent and the error is saved.
	try :
		#It is checked if the coordinates are not in the given list,  if they are, an error 400 is returned.
		for coordinates in mkad_km :
			if coordinates[1] == longPoint and coordinates[2] == latPoint :
				return {"msg": "Invalid Lat or Long value"}, 400

		#The distance between the coordinates is obtained in miles and they are converted into km.
		miles = round(geodesic((latMRR, longMRR), (latPoint, longPoint)).miles, 2)
		km = round(miles * 1.60934, 2)
		
		
		return {"msg": "successful", "result": {"miles": miles, "km": km}}, 200

	except Exception as error:
		return None, error

