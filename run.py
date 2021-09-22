"""
Created on Tues Sep 21 12:40:00 2021

@author: Luis Esteban Fortanel Hernandez
"""

from app import create_app
#The app is created calling the function.
app = create_app('testing') 
#The app is run defining the host and port.
app.run(host= '0.0.0.0', port = 5000)