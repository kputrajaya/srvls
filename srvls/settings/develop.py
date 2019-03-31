from .base import *  # noqa: F401 F403
from .base import INSTALLED_APPS, MIDDLEWARE


INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ['127.0.0.1']
