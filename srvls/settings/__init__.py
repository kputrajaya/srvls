import os

ENVIRONMENT = os.environ.get('DJANGO_SETTINGS_MODULE', '')

if ENVIRONMENT == 'srvls.settings':
    from .develop import *  # noqa: F401 F403
