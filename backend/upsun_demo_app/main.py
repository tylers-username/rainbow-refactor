"""
This module sets up the Flask application and its configurations.

It initializes the Flask app, sets up CORS, loads environment variables,
configures session management (commented out, pending Redis implementation),
registers the routes, and runs the app with the specified port and debug settings.
"""

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app import routes

# from flask_session import Session


def create_app():
    """
    Create and configure an instance of the Flask application.

    Environment variables are loaded, the Flask app is initialized, and
    Redis configuration for sessions is set up if available. Routes are
    also registered with the application instance before it is returned.
    """
    # Bring in environment variables
    load_dotenv()

    # Initialize app
    flask_app = Flask(__name__)

    # Use Redis for Sessions if available
    # if 'implement redis but consider how to handle in local dev environment':
    #     app.config['SESSION_TYPE'] = 'redis'  # Session storage type
    #     app.config['SESSION_PERMANENT'] = False  # Make the sessions non-permanent
    #     app.config['SESSION_USE_SIGNER'] = True  # Securely sign the session cookie
    #     app.config['SESSION_KEY_PREFIX'] = 'session:'  # Prefix for storing session data in Redis
    #     app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379, db=0)

    #     sess = Session()
    #     sess.init_app(app)

    flask_app.register_blueprint(routes.bp)

    return flask_app


app = create_app()
CORS(app)

if __name__ == "__main__":
    flask_environment = os.environ.get("FLASK_ENV", "local")
    enable_debug = flask_environment != "production"
    web_port = os.environ.get("PORT", 8000)
    app.run(port=web_port, debug=enable_debug)
