from .base import *  # noqa: F401 F403
from .base import AWS_LOG_GROUP


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
        'simple': {
            'format': '[%(levelname)-8s] %(message)s'
        }
    },
    'handlers': {
        'cloudwatch': {
            'class': 'watchtower.django.DjangoCloudWatchLogHandler',
            'log_group': f'{AWS_LOG_GROUP}/logs',
            'send_interval': 15,
            'formatter': 'simple'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['cloudwatch']
        }
    },
}

STATICFILES_STORAGE = 'srvls.aws.StaticStorage'
DEFAULT_FILE_STORAGE = 'srvls.aws.MediaStorage'
MEDIA_ROOT = '/tmp/media/'
STATIC_ROOT = '/tmp/static/'
