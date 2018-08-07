"""
This script runs the Attendee Predictor application using a development server.
"""

from os import environ
from Attendee_Predictor import app # imports the code from Attendee_Predictor/__init__.py

# WSGI interface available at the top level for wfastcgi to access it
wsgi_app = app.wsgi_app

# check if the executed file is the main program and run the app
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True) # print traceback to console