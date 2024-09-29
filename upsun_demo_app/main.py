"""
This module sets up the Flask application and its configurations.

It initializes the Flask app, sets up CORS, loads environment variables,
configures session management (commented out, pending Redis implementation),
registers the routes, and runs the app with the specified port and debug settings.
"""

import os
from flask import Flask, url_for
from flask_cors import CORS
from dotenv import load_dotenv
from upsun_demo_app import routes


# from flask_session import Session

def create_app():
    """
    Create and configure an instance of the Flask application.

    Environment variables are loaded, the Flask app is initialized, and
    Redis configuration for sessions is set up if available. Routes are
    also registered with the application instance before it is returned.
    """
    # Load environment variables from .env
    load_dotenv()

    # Initialize Flask app
    flask_app = Flask(__name__)

    # Configure Environment
    flask_env = os.getenv("FLASK_ENV", "production")
    flask_app.config['ENV'] = flask_env
    flask_app.config['DEBUG'] = flask_env != "production"

    # Apply CORS
    CORS(flask_app)

    # Optionally configure Redis for Sessions
    # if 'implement redis but consider how to handle in local dev environment':
    #     flask_app.config['SESSION_TYPE'] = 'redis'  # Session storage type
    #     flask_app.config['SESSION_PERMANENT'] = False  # Make the sessions non-permanent
    #     flask_app.config['SESSION_USE_SIGNER'] = True  # Securely sign the session cookie
    #     flask_app.config['SESSION_KEY_PREFIX'] = 'session:'  # Prefix for storing session data in Redis
    #     flask_app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379, db=0)
    #
    #     sess = Session()
    #     sess.init_app(flask_app)

    # Register blueprints or routes
    flask_app.register_blueprint(routes.bp)

    # Context Processor to inject 'debug' into templates
    @flask_app.context_processor
    def inject_debug():
        return {'debug': flask_app.debug}

    def versioned_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                file_path = os.path.join(flask_app.root_path, 'static', filename)
                if os.path.isfile(file_path):
                    # Use the file's last modification time as the version
                    values['v'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)

    # Register the helper function globally
    flask_app.jinja_env.globals['versioned_url_for'] = versioned_url_for


    return flask_app


def dev_server(app, port):
    """
    Start the development server with Livereload.

    Args:
        app (Flask): The Flask application instance.
        port (int): The port number to run the server on.
    """
    from livereload import Server

    server = Server(app.wsgi_app)

    # Watch templates and static files
    server.watch('**/*.html')
    server.watch('**/*.css')
    server.watch('**/*.js')

    def warn_env_change():
        print("\n\n.env has been updated. You will need to manually restart the server\n\n")

    server.watch('.env', warn_env_change)

    # Watch Python files to restart the server
    server.watch('**/*.py')

    print(f"Starting development server with LiveReload on port {port}")
    server.serve(host='0.0.0.0', port=port, debug=True, open_url_delay=1)


def run_production(app, port):
    """
    Placeholder for running the production server.

    In production, it's recommended to use a WSGI server like Gunicorn.

    Args:
        app (Flask): The Flask application instance.
        port (int): The port number to run the server on.
    """
    print("Running in production mode. Set FLASK_ENV=local or use Gunicorn to serve the production app.")
    print(f"Example Gunicorn command: \n\tpoetry run gunicorn -w 4 -b 0.0.0.0:{port} upsun_demo_app.main:app")
    print(f"\tOr poetry run app-serve")
    # Example:
    # gunicorn -w 4 -b 0.0.0.0:8000 upsun_demo_app.main:app


# Create the Flask app
app = create_app()

def main():
    """
    Entry point for running the Flask application via Poetry script.

    Determines the environment and starts the appropriate server.
    """
    # Load environment variables
    load_dotenv()

    # Determine environment and port
    flask_env = os.getenv("FLASK_ENV", "production")
    enable_debug = flask_env != "production"
    try:
        web_port = int(os.getenv("PORT", 8000))
    except ValueError:
        print("Invalid PORT environment variable. Using default port 8000.")
        web_port = 8000

    if enable_debug:
        # Start development server with Livereload
        dev_server(app, web_port)
    else:
        # Start production server (suggest using Gunicorn)
        run_production(app, web_port)



# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
