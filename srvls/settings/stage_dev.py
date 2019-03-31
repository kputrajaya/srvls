from .base import *  # noqa: F401 F403
from .base import AWS_STORAGE_BUCKET_NAME


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'db.sqlite3',
        'BUCKET': 'srvls-db'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'aws': {
            'format': '%(asctime)s [%(levelname)-8s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'cloudwatch': {
            'level': 'DEBUG',
            'class': 'watchtower.CloudWatchLogHandler',
            'log_group': AWS_STORAGE_BUCKET_NAME,
            'formatter': 'aws'
        }
    },
    'loggers': {
        'django': {
            'level': 'WARNING',
            'handlers': ['cloudwatch']
        },
        'master': {
            'level': 'INFO',
            'handlers': ['cloudwatch']
        }
    },
}

STATICFILES_STORAGE = 'srvls.aws.StaticStorage'
DEFAULT_FILE_STORAGE = 'srvls.aws.MediaStorage'
MEDIA_ROOT = '/tmp/media/'
STATIC_ROOT = '/tmp/static/'
