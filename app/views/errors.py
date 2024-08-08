# Imports
from flask import Blueprint, render_template

errors_bp = Blueprint("errors", __name__)

@errors_bp.app_errorhandler(400)
def bad_request(e):
    """Handles 400 Bad Request errors."""
    return (
        render_template(
            "error.html",
            error_title="400. That's an error.",
            error_desc="Bad request received.",
        ),
        400,
    )

@errors_bp.app_errorhandler(401)
def unauthorized(e):
    """Handles 401 Unauthorized errors."""
    return (
        render_template(
            "error.html",
            error_title="401. That's an error.",
            error_desc="You are not authorized to access this page.",
        ),
        401,
    )

@errors_bp.app_errorhandler(403)
def error_forbidden(e):
    """Handles 403 Forbidden errors."""
    return (
        render_template(
            "error.html",
            error_title="403. That's an error.",
            error_desc="This page is forbidden.",
        ),
        403,
    )

@errors_bp.app_errorhandler(404)
def not_found(e):
    """Handles 404 Not Found errors."""
    return (
        render_template(
            "error.html",
            error_title="404. That's an error.",
            error_desc="The requested page was not found on this server.",
        ),
        404,
    )

@errors_bp.app_errorhandler(503)
def unavailable(e):
    """Handles 503 Service Unavailable errors."""
    return (
        render_template(
            "error.html",
            error_title="503. That's an error.",
            error_desc="Service unavailable.",
        ),
        503,
    )
