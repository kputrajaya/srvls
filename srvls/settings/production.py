from .base import *  # noqa: F401 F403

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'db.sqlite3',
        'BUCKET': 'srvls-db'
    }
}

STATIC_URL = 'https://cdn-srvls.kputrajaya.com/static/'
