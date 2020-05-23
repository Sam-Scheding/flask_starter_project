import re


class ValidationService:


    def is_valid_email(email):
        if email in [None, '']:
            return False

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False

        return True


    def is_valid_password(password):
        if password in [None, '']:
            return False

        if len(password) < 8:
            return False

        # TODO: Check for special characters/numbers
        # TODO: Check common passwords

        return True
