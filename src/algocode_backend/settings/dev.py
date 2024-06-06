from .base import * # noqa 
from .base import env  # noqa: E501 
# warnigns for linters code - E501 for unused variables


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="5b39bcce08a6a7d7168a4b1b5c43143d021f672ebf50c5aff0d6dd7c30a4",
)

DEBUG = True 

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "http://127.0.0.1:8080"]

ALLOWED_HOSTS = ["127.0.0.1"]


# EMAIL BACKEND #
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
DOMAIN = env("EMAIL_DOMAIN")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "iammahboob.a@gmail.com"
SITE_NAME = "Algocode Backend"


########################################################
# logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s  %(process)d %(thread)d %(message)s "
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    # uncomment for django database query logs
    # 'loggers': {
    #     'django.db': {
    #         'level': 'DEBUG',
    #         'handlers': ['console'],
    #     }
    # }
}
