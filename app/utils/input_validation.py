# Imports
# ---
import re
# ---


class Validate:
    """
    A class containing static methods to validate various types of user input, 
    including email addresses, phone numbers, and names.
    """

    @staticmethod
    def email_address(inp: str) -> bool:
        """
        Validates an email address using a regular expression.

        This method checks if the provided input string is a valid email address
        according to a specific regular expression pattern.

        Args:
            inp (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        # https://www.javatpoint.com/how-to-validated-email-address-in-python-with-regular-expression
        pattern = re.compile(
            r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
        )
        if re.fullmatch(pattern, inp):
            return True
        return False

    @staticmethod
    def phone_number(inp: str) -> bool:
        """
        Validates a phone number based on a specific pattern.

        This method checks if the provided input string is a valid phone number
        that matches the expected format (Sri Lankan phone numbers in this case).

        Args:
            inp (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        # https://stackoverflow.com/a/51521420
        pattern = re.compile(r"^(?:7|0|\+94)[0-9]{9,10}$")
        if re.fullmatch(pattern, inp):
            return True
        return False

    @staticmethod
    def name(inp: str) -> bool:
        """
        Validates a name to ensure it contains only alphabetic characters.

        This method checks if the provided input string is a valid name
        consisting solely of alphabetic characters.

        Args:
            inp (str): The name to validate.

        Returns:
            bool: True if the name contains only alphabetic characters, False otherwise.
        """
        if inp.isalpha():
            return True
        return False