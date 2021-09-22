# Test Task Luis Esteban Fortanel Hernandez
This is the code to find the distance from the Moscow Ring Road to the specified address through a service developed by a Flask Blueprint.

# How to install
Clone de repo with the following command:

git clone https://github.com/LuisFort/Test_Task_LuisFortanel.git


*****This project runs in Python3.7*****
 
To run the code it is necessary to install the libraries that are in the requirements.txt file.

# How to use

Once the libraries are installed, you just have to run the code like this:

	python run.py

***Make sure you are in the folder of the project.***



To test the service you can use the browser (I suggest postman to make it look better), using the url:

	http://0.0.0.0:5000/calculateDistance?lat=55.883555&long=37.723633

Change the latitude and longitude values to test more coordinates.



You can use the file UnitTest.py to test the calculationDistance function using the following command:

	python UnitTest.py --latitude 55.883555 --longitude 37.723633


