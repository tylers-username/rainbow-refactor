"""
This module sets defines the routes for your Flask application
"""

import os
import base64
import json
from flask import Blueprint, jsonify

bp = Blueprint("routes", __name__)

SERVICE_RELATIONSHIP = "redis_session"

API_PREFIX = "/api/v1"


@bp.route(f"{API_PREFIX}/environment")
def environment():
    """
    Returns the environment type and sessions storage type as json
    """
    return jsonify(
        type=get_platform_environment(), session_storage=get_session_storage_type()
    )


@bp.route("/api/")
def home():
    """
    Returns a welcome message for the home route.
    """
    return "Hello from the Python backend!"


def get_session_storage_type():
    """
    Returns the type of session storage from the PLATFORM_RELATIONSHIPS environment variable.
    If the variable is not set or if it does not contain the SERVICE_RELATIONSHIP, it returns "file"
    If the variable is set and contains the SERVICE_RELATIONSHIP, it returns "redis".
    If there is an error decoding the PLATFORM_RELATIONSHIPS variable, it returns "file".
    """
    platform_relationships_data = os.environ.get("PLATFORM_RELATIONSHIPS")

    if not platform_relationships_data:
        return "file"

    try:
        platform_relationships = json.loads(
            base64.b64decode(platform_relationships_data)
        )

        if SERVICE_RELATIONSHIP in platform_relationships:
            return "redis"

        return "file"
    except (json.JSONDecodeError, TypeError, ValueError):
        # Catching potential exceptions due to invalid JSON or other issues
        return "file"


def get_platform_environment():
    """
    Returns the type of the environment from PLATFORM_ENVIRONMENT_TYPE environment variable.
    If the variable is not set, it returns "local".
    """
    return os.environ.get("PLATFORM_ENVIRONMENT_TYPE", "local")
