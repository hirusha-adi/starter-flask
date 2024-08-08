# Imports
# ---
import typing as t
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user
from flask.wrappers import Response
from werkzeug.wrappers import Response as BaseResponse

from app.extensions import sitemapper
from app.logging_config import logger
# ---


main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@main_bp.route("/terms-and-conditions", methods=["GET"])
def terms_and_conditions() -> str:
    return render_template("terms_and_conditions.html")


@main_bp.route("/privacy-policy", methods=["GET"])
def privacy_policy() -> str:
    return render_template("privacy_policy.html")


@main_bp.route("/refund-policy", methods=["GET"])
def refund_policy() -> str:
    return render_template("refund_policy.html")


@main_bp.route("/faq", methods=["GET"])
def faq_page() -> str:
    return render_template("faq.html")


@main_bp.route("/sitemap.xml")
def sitemap() -> Response:
    return sitemapper.generate()
