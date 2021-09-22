#python UnitTest.py --latitude 55.883555 --longitude 37.723633
import argparse
from app.distance.Controller import calculateDistance as cd

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-lat", "--latitude", required=True,
	type = float, help="the latitude of the address")
ap.add_argument("-long", "--longitude", required=True,
	type=float, help="the longitude of the address")

args = vars(ap.parse_args())

#getting the values
latitude = args["latitude"]
longitude = args["longitude"]


dict_response, status_code = cd(latitude, longitude)
if dict_response :
	print(dict_response, status_code)
else :
	print("Error calculating the distance")