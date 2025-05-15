import os


class Config:
    SECRET_KEY = os.environ.get('9151409360a2e1974325a87a9dd7473d') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
