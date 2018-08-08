"""
This script runs the Attendee Predictor application using a development server.
"""

from os import environ
from Attendee_Predictor import app # imports the code from Attendee_Predictor/__init__.py

# check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) # print traceback to console