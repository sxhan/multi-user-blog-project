import re
import logging

import models
import auth


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def validate_username(text):
    valid = True
    error = None
    # Check username validity
    if not USER_RE.match(text):
        error = ("username_error", "Invalid Username")
        return False, error

    # check for exisitng username
    existing_users = models.User.all().filter("username =", text).count()
    if existing_users > 0:
        return False, ("username_error", "Username taken!")

    return valid, error


def validate_password(text):
    valid = True
    error = None
    if not PASSWORD_RE.match(text):
        return False, ("password_error", "Invalid Password")
    return valid, error


def validate_verify(password, verify):
    valid = True
    error = None
    if not password == verify:
        return False, ("password_error", "Passwords do not match!")
    return valid, error


def validate_email(text):
    valid = True
    error = None
    if text:
        if not EMAIL_RE.match(text):
            return False, ("email_error", "Invalid Email")
        return valid, error
    return valid, error


def validate_login_user(text):
    valid = True
    error = None
    existing_users_count = models.User.all().filter("username =", text).count()
    if existing_users_count != 1:
        return False, ("username_error", "Invalid Username")
    return valid, error


def validate_login_password(username, password):
    valid = True
    error = None
    existing_user = models.User.all().filter("username =", username).get()
    if not existing_user:
        return False, None
    hashed_pw = existing_user.password
    salt = hashed_pw.split("|")[1]
    logging.info("hasked_pw: %s" % hashed_pw)
    logging.info("salt: %s" % salt)
    logging.info("username: %s" % username)
    logging.info("password: %s" % password)
    logging.info("pw_hash: %s" % auth.make_pw_hash(username + password, salt))
    if auth.make_pw_hash(username, password, salt) != hashed_pw:
        return False, ("password_error", "Invalid Password")
    return valid, error


def validate_login(username="", password=""):
    """Returns a tuple of (pass_validation, errors)

    pass_validation: is a boolean indicating if the signup is valid
    errors: is a list of tuples of ("{{error_key}}", "{{error_message}}")
    pairs
    """
    pass_validation = True
    errors = []
    validations = [validate_login_user(username),
                   validate_login_password(username, password)]
    for valid, error in validations:
        logging.info(valid)
        logging.info(error)
        pass_validation &= valid
        if error:
            errors.append(error)
    return pass_validation, errors


def validate_signup(username="", password="", verify="", email=""):
    """Returns a tuple of (pass_validation, errors)

    pass_validation: is a boolean indicating if the signup is valid
    errors: is a list of tuples of ("{{error_key}}", "{{error_message}}")
    pairs
    """
    pass_validation = True
    errors = []
    validations = [validate_username(username),
                   validate_password(password),
                   validate_verify(password, verify),
                   validate_email(email)]
    for valid, error in validations:
        pass_validation &= valid
        if error:
            errors.append(error)
    return pass_validation, errors
