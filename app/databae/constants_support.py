# Imports
# ---
import typing as t
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.logging_config import logger
from app.models import Constant, db
from app import errors
# ---


class Constant_Support:
    """
    A class that provides support for creating, retrieving, and updating constants
    in the database.
    """
    
    @staticmethod
    def create_constant(key: str, value: str) -> t.Optional[Constant]:
        """
        Creates a new constant in the database.

        This method attempts to create a new constant with the provided key and value.
        If a constant with the same key already exists, it will log a warning and return `None`.
        Handles SQL-related exceptions and logs errors as necessary.

        Args:
            key (str): The key for the constant.
            value (str): The value for the constant.

        Returns:
            Optional[Constant]: The newly created `Constant` object if successful, 
            or `None` if the constant already exists or an error occurs.
        """
        try:
            ticket_price = Constant.query.filter_by(key=key).first()
            if ticket_price is None:
                new_constant = Constant(key=key, value=value)  # type: ignore
                db.session.add(new_constant)
                db.session.commit()
                logger.info(f"Constant {key} created successfully.")
                return new_constant
            else:
                logger.warning(f"Constant {key} already exists.")
        except IntegrityError:
            db.session.rollback()
            logger.error(f"IntegrityError: Duplicate key {key} found.", exc_info=True)
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"SQLAlchemyError: {str(e)}", exc_info=True)
        except Exception as e:
            db.session.rollback()
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)

    @staticmethod
    def get_constant(key: str) -> t.Optional[Constant]:
        """
        Retrieves a constant from the database.

        This method retrieves the constant associated with the provided key from the database.
        Logs whether the constant was found or not, and handles SQL-related exceptions.

        Args:
            key (str): The key of the constant to retrieve.

        Returns:
            Optional[Constant]: The `Constant` object if found, or `None` if the constant 
            does not exist or an error occurs.
        """
        try:
            constant = Constant.query.filter_by(key=key).first()
            if constant:
                logger.debug(f"Constant {key} retrieved successfully.")
            else:
                logger.error(f"Constant {key} not found.")
            return constant
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemyError: {str(e)}", exc_info=True)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return None

    @staticmethod
    def update_constant(key: str, value: str) -> t.Optional[Constant]:
        """
        Updates the value of an existing constant in the database.

        This method updates the value of the constant associated with the provided key.
        Logs the update operation and handles SQL-related exceptions.

        Args:
            key (str): The key of the constant to update.
            value (str): The new value for the constant.

        Returns:
            Optional[Constant]: The updated `Constant` object if successful, or `None` 
            if the constant does not exist or an error occurs.
        """
        try:
            constant = Constant.query.filter_by(key=key).first()
            if constant:
                constant.value = value
                db.session.commit()
                logger.info(f"Updating: {key} to {value}")
                return constant
            else:
                raise errors.RecordNotFound(f"No `constant` record found for: {key}. Unable to update the value!")
        except IntegrityError:
            db.session.rollback()
            logger.error(f"IntegrityError: Duplicate key {key} found.", exc_info=True)
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"SQLAlchemyError: {str(e)}", exc_info=True)
        except Exception as e:
            db.session.rollback()
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return None
