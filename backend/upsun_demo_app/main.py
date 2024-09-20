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
from upsun_demo_app import routes
from livereload import Server
# from flask_session import Session

def dev_server():
    load_dotenv()
    flask_environment = os.getenv("FLASK_ENV", "local")
    enable_debug = flask_environment != "production"
    web_port = int(os.getenv("PORT", 8000))

    if enable_debug:
        # Development server with LiveReload
        server = Server(app.wsgi_app)
        # Watch templates and static files
        server.watch('templates/**/*.html')
        server.watch('static/**/*.*')
        # Watch Python files to restart the server
        server.watch('**/*.py')
        print(f"Starting development server with LiveReload on port {web_port}")
        server.serve(host='0.0.0.0', port=web_port, debug=True, open_url_delay=1)
    else:
        # Production server with Gunicorn
        print("Running in production mode. Use Gunicorn to serve the app.")

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
app.debug = (os.environ.get("FLASK_ENV", "local") == "local")
CORS(app)

if __name__ == "__main__":
    flask_environment = os.environ.get("FLASK_ENV", "local")
    enable_debug = flask_environment != "production"
    web_port = os.environ.get("PORT", 8000)
    app.run(port=web_port, debug=enable_debug)
