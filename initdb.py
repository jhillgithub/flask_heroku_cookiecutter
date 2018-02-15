from {{cookiecutter.app_name}}.app import db
import os

if bool(os.environ.get('DEVELOPMENT', '')):
    db.drop_all()
db.create_all()
