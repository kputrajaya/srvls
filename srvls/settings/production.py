from .base import *  # noqa: F401 F403
from .base import INSTALLED_APPS

INSTALLED_APPS.append('zappa_django_utils')

DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'db.sqlite3',
        'BUCKET': 'srvls-db'
    }
}
