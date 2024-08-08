# Imports
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import event
from app.config import SuperAdmin
from app.extensions import db
from app.logging_config import logger


class Constant(db.Model):
    __tablename__ = "constants"
    key = db.Column(db.String(255), primary_key=True)
    value = db.Column(db.String(255), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True)
    is_super_admin = db.Column(db.Boolean, nullable=True)
    registered_at = db.Column(db.DateTime, nullable=False)

    def get_id(self):
        return self.user_id


# Based on: https://stackoverflow.com/a/62226934/14819138
@event.listens_for(User.__table__, "after_create")  # type: ignore
def create_users(*args, **kwargs):
    db.session.add(
        User(  # type: ignore
            first_name=SuperAdmin.SUPER_ADMIN_FIRST_NAME,
            last_name=SuperAdmin.SUPER_ADMIN_LAST_NAME,
            email=SuperAdmin.SUPER_ADMIN_EMAIL,
            password=SuperAdmin.SUPER_ADMIN_PASSWORD,
            is_admin=True,
            is_super_admin=True,
            registered_at=datetime.now(),
        )
    )
    db.session.commit()
    logger.debug("Created super admin user on `after_create` event")
    