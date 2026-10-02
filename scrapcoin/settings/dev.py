from .base import *

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scrapcoin_db',
        'USER': 'postgres',
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'db',
        'PORT': '5432',
    }
}