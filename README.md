Test Task Luis Esteban Fortanel Hernandez
==============

My Test

This is the code to find the distance from the Moscow Ring Road to the specified address through a service developed by a Flask Blueprint.

To run the code it is necessary python 3.7.4 and install the libraries that are in the requirements.txt file.

Once the libraries are installed, you just have to run the code like this
--->       python run.py

To test the service you can use the browser (I suggest postman to make it look better), using the url 
	http://0.0.0.0:5000/calculateDistance?lat=55.883555&long=37.723633
Change the latitude and longitude values to test more coordinates.

You can use the file UnitTest.py to test the calculation of the distance between coordinates.
