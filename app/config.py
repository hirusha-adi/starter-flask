# Imports
# ---
import os
from dotenv import load_dotenv
# ---

# Learn more at: https://pypi.org/project/python-dotenv
load_dotenv()


class ConfigApp:
    # Configuration for Flask App
    FLASK_ENV: str = str(os.getenv("FLASK_ENV"))
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")
    ENVIRONMENT_NAME: str = str(os.getenv("ENVIRONMENT_NAME"))
    IS_PROD = ENVIRONMENT_NAME.startswith("dev")

    # Database Configuration
    # MYSQL_USERNAME: str = str(os.getenv("MYSQL_USERNAME"))
    # MYSQL_PASSWORD: str = str(os.getenv("MYSQL_PASSWORD"))
    # MYSQL_HOST: str = str(os.getenv("MYSQL_HOST"))
    # MYSQL_DATABASE: str = str(os.getenv("MYSQL_DATABASE"))
    SQLALCHEMY_DATABASE_URI: str = (
        f"sqlite:///database.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    

class SuperAdmin:
    # Default Super Admin Account
    SUPER_ADMIN_FIRST_NAME: str = str(os.getenv("SUPER_ADMIN_FIRST_NAME"))
    SUPER_ADMIN_LAST_NAME: str = str(os.getenv("SUPER_ADMIN_LAST_NAME"))
    SUPER_ADMIN_EMAIL: str = str(os.getenv("SUPER_ADMIN_EMAIL"))
    SUPER_ADMIN_PASSWORD: str = str(os.getenv("SUPER_ADMIN_PASSWORD"))


class Other:
    # Program Logging
    LOG_TO_FILE: str = str(os.getenv("LOG_TO_FILE", "True"))
    # BugSnag API Key, Get it from: https://www.bugsnag.com/
    BUGSNAG_API_KEY: str = str(os.getenv("BUGSNAG_API_KEY"))