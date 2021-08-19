"""
Production settings for digital ocean
"""

import environ

from src.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': ('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}