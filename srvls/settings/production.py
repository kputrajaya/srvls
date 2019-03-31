from boto3.session import Session

from .base import *  # noqa: F401 F403
from .base import (
    AWS_ACCESS_KEY_ID,
    AWS_S3_REGION_NAME,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME
)


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
            # 'boto3_session': Session(
            #     aws_access_key_id=AWS_ACCESS_KEY_ID,
            #     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            #     region_name=AWS_S3_REGION_NAME
            # ),
            'log_group': AWS_STORAGE_BUCKET_NAME,
            'formatter': 'aws'
        }
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['cloudwatch'],
            'propagate': False
        }
    },
}

STATICFILES_STORAGE = 'srvls.aws.StaticStorage'
DEFAULT_FILE_STORAGE = 'srvls.aws.MediaStorage'
MEDIA_ROOT = '/tmp/media/'
STATIC_ROOT = '/tmp/static/'
