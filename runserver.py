"""
This script runs the Attendee Predictor application using a development server.
"""

from os import environ
from attendee_predictor import app

# check if the executed file is the main program and run the app
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, debug=True) # print traceback to console