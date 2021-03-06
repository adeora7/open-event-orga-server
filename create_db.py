import re
import sys

from open_event import current_app
from open_event.models import db

from open_event.helpers.data import DataManager
from populate_db import populate


def _validate_email(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print '\nInvalid email address'
        sys.exit(1)


def _validate_password(password):
    if len(password) < 4:
        print '\nPassword should have minimum 4 characters'
        sys.exit(1)


def create_default_user():
    print "Your login is 'super_admin'."
    email = raw_input("Enter email for super_admin    : ")
    _validate_email(email)
    password = raw_input("Enter password for super_admin : ")
    _validate_password(password)
    DataManager.create_super_admin(email, password)


if __name__ == "__main__":
    with current_app.app_context():
        db.create_all()
        create_default_user()
        populate()
