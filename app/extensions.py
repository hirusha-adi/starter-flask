# Imports
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sitemapper import Sitemapper
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
sitemapper = Sitemapper()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from app.models import User

    return User.query.get(int(user_id))