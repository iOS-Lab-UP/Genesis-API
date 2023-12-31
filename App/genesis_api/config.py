from dotenv import load_dotenv

import os
import secrets
import redis


# Specify the path to your .env file if it's not in the same directory as this file
dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
# Load the .env file
load_dotenv(dotenv_path)


class Config:

    # SQL Credentials
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_PORT = os.getenv("MYSQL_PORT")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # JWT Secret Key
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Mail Credentials
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
    MAIL_EMAIL = os.environ.get(
        "MAIL_EMAIL")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # URL for redis
    RATELIMIT_STORAGE_URL = os.environ.get(
        "REDIS_URL", 'redis://redis_rate_limiting:6379')

    # URL for uploading pdfs
    UPLOAD_FOLDER = os.environ.get(
        "UPLOAD_FOLDER", 'App/genesis_api/static/uploads')

    REDIS_CLIENT = redis.StrictRedis(
        host='redis_sessions', port=6379, decode_responses=True, db=0)
    REDIS_JWT_CLIENT = redis.StrictRedis(
        host='redis_sessions', port=6379, db=1, decode_responses=True)

    CACHE_CONFIG = {
        "DEBUG": True,          # some Flask specific configs
        "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
        "CACHE_DEFAULT_TIMEOUT": 300
    }

    # check if the folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
