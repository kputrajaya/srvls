from .base import *  # noqa: F401 F403
from .base import MIDDLEWARE


MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ['127.0.0.1']
