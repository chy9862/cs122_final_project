"""This is the main file to run the application.

This file is used to run the application. It imports the create_app function from the
app package and creates an instance of the Flask application. The application is then
run in debug mode.

Attributes:
    app: An instance of the Flask application.
    create_app: A function that creates an instance of the Flask application.
    Flask: A class that creates an instance of the Flask application.

Typical usage example:
    app.run(debug=True)
"""

from app import create_app
from flask import Flask

# Create an instance of the Flask application
app = create_app()

# Run the application
if __name__ == "__main__":
    # Run the application in debug mode
    app.run(debug=True)
