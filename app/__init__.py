# Imports
import bugsnag
from bugsnag.flask import handle_exceptions
from flask import Flask
from app.config import ConfigApp, Other
from app.extensions import csrf, db, login_manager, migrate, sitemapper
from app.logging_config import logger


def create_app() -> Flask:
    # Init Flask
    # ---
    app = Flask(__name__)
    app.config.from_object(ConfigApp)
    # ---

    logger.debug("Intantiated flask app")

    # Init Extensions
    # ---
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "user.login"  # type: ignore
    sitemapper.init_app(app)
    csrf.init_app(app)
    # ---

    logger.debug("Intantiated extensions")

    # Bugsnag
    # ---
    if ConfigApp.IS_PROD:
        bugsnag.configure(
            api_key=Other.BUGSNAG_API_KEY,
            project_root="/",
        )
        handle_exceptions(app)
        logger.debug("Intantiated BugSnag")
    # ---

    # Setup Blueprints
    # ---

    # Blueprints
    from app.views.main import main_bp
    from app.views.erros import errors_bp

    # Main blueprints
    app.register_blueprint(main_bp) # main public routes, at /
    app.register_blueprint(errors_bp) # error pages

    # Admin Blueprints
    app.register_blueprint(admin_users_bp, url_prefix="/admin/users")
    app.register_blueprint(admin_contactus_bp, url_prefix="/admin/contact-us")

    # Add other blueprints
    # app.register_blueprint(other_bp, url_prefix="/other_route")
    # app.register_blueprint(other_long_bp, url_prefix="/other/route")

    # ---

    logger.debug("Registered blueprints")

    # Database setup
    # ---
    with app.app_context():
        db.create_all()
    # ---

    logger.debug("Intantiated the database")

    # Sitemap setup
    # ---
    sitemapper.add_endpoint("main.index")
    sitemapper.add_endpoint("main.terms_and_conditions")
    sitemapper.add_endpoint("main.privacy_policy")
    sitemapper.add_endpoint("main.refund_policy")
    sitemapper.add_endpoint("main.faq_page")
    sitemapper.add_endpoint("main.contact_us")
    sitemapper.add_endpoint("user.login")
    sitemapper.add_endpoint("user.register")
    sitemapper.add_endpoint("user.forgot_password")
    # ---

    logger.debug("Intantiated sitemaps")

    logger.info("Application created.")

    return app