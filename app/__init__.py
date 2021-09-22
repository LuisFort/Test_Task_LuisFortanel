"""
Created on Tues Sep 21 12:40:00 2021

@author: Luis Esteban Fortanel Hernandez
"""

from config import config, Flask, logging, CORS
from .distance import distance as blueprintDistance

"""
***********************************************************************
Create the app
***********************************************************************
Description:
    The function creates the app and configures it to use 
    the blueprint and save the logs

Requirements: 
    The enviroment for the app (develoment, testing or production).
    
Return:
    App

***********************************************************************
"""

def create_app(config_name):
	#Setting up the app
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	# Setting up the blueprint
	app.register_blueprint(blueprintDistance)

	#Setting up the logs, the format string and the configuration
	logFormatStr = '[%(asctime)s]  %(levelname)s - %(message)s'
	logging.basicConfig(format = logFormatStr, level = logging.DEBUG)
	formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')



	#Creating and setting up the .log file to save the data
	fileHandler = logging.FileHandler(".log")
	fileHandler.setLevel(logging.INFO)
	fileHandler.setFormatter(formatter)
	app.logger.addHandler(fileHandler)

	#Setting up the logs in the console
	streamHandler = logging.StreamHandler()
	streamHandler.setLevel(logging.DEBUG)
	streamHandler.setFormatter(formatter)
	app.logger.addHandler(streamHandler)

	#First log
	app.logger.info("Initializing the app")

	#setting up the CORS
	CORS(app)
	return app