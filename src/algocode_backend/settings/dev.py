from .base import * # noqa 
from .base import env  # noqa: E501 
# warnigns for linters code - E501 for unused variables


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-1b85e9_7riupf=te$-7k(qr2a#8a6z$0+m4zht&34avjt!*c8l",
)

DEBUG = True 

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "http://127.0.0.1:8080"]

ALLOWED_HOSTS = ["127.0.0.1"]
