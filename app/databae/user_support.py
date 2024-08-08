# Imports
# ---
import typing as t
from datetime import datetime
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.logging_config import logger
from app.models import User, db
# ---

class User_Support:
    """
    A class for supporting operations related to users.

    This class contains static methods for creating users in the database
    and handling different exceptions that may arise during the process.
    """

    @staticmethod
    def create_user(
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        is_admin: t.Optional[bool] = True,
        is_super_admin: t.Optional[bool] = True,
    ) -> t.Union[User, str]:
        """
        Creates a new user in the database.

        This method attempts to create a new user in the database with the provided
        details. It handles various exceptions, including `IntegrityError` for duplicate
        entries and `SQLAlchemyError` for general SQLAlchemy exceptions. Super admin
        permissions are set up hierarchically, where a super admin is also an admin.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email address of the user.
            password (str): The password for the user account. This should be hashed before
                being stored in the database.
            is_admin (bool, optional): A boolean indicating if the user is an admin. Defaults to True.
            is_super_admin (bool, optional): A boolean indicating if the user is a super admin.
                Defaults to True. Super admins are also considered admins.

        Returns:
            User: The newly created user object if successful.
            str: An error message if the operation failed.
        """

        # Hash the password
        # ---
        # from werkzeug.security import generate_password_hash
        # hashed_password = generate_password_hash(password, method='sha256')
        # ---

        try:
            already_existing_user = User.query.filter_by(email=email).first()
            if already_existing_user is None:

                # setup super admin permissions properly 
                # in a hierarchical manner
                if is_super_admin:
                    is_admin = True

                new_user = User(  # type: ignore
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    is_admin=is_admin,
                    is_super_admin=is_super_admin,
                    registered_at=datetime.now(),
                )

                db.session.add(new_user)
                db.session.commit()
                logger.info(f"User ({first_name} {last_name} - {email}) created successfully.")
                return new_user

            else:
                logger.warning(f"User with the email:{email} already exists!")
                return f"Error: User with that email already exists!"

        except IntegrityError:
            db.session.rollback()
            logger.error(f"IntegrityError: A user with email {email} already exists.", exc_info=True)
            return "Error: A user with this email already exists."

        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"SQLAlchemyError: {str(e)}", exc_info=True)
            return f"Error: {str(e)}"

        except Exception as e:
            db.session.rollback()
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            return f"Error: {str(e)}"
