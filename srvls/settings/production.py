from .base import *  # noqa: F401 F403

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'db.sqlite3',
        'BUCKET': 'srvls-db'
    }
}

STATICFILES_STORAGE = 'srvls.aws.StaticStorage'
DEFAULT_FILE_STORAGE = 'srvls.aws.MediaStorage'

MEDIA_ROOT = '/tmp/media'
STATIC_ROOT = '/tmp/static'
