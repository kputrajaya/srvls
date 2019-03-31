import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '8m3^x8)**@&9^bgq1t3=p#x0#uysw*a_237mevdi0%*_6s1@$d'

DEBUG = True

ALLOWED_HOSTS = ('*',)


# Application definition

INSTALLED_APPS = [
    'master',

    'debug_toolbar',
    'zappa_django_utils',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'srvls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'srvls.wsgi.application'

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Caching and session
# https://docs.djangoproject.com/en/2.1/ref/settings/#cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'app-cache',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


# Email
# https://docs.djangoproject.com/en/2.1/topics/email/

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MAILGUN_USER')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Kevin <no-reply@kputrajaya.com>'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


# Third party settings

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = os.environ.get('AWS_REGION')
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = os.environ.get('CDN_DOMAIN')
AWS_S3_OBJECT_PARAMETERS = {'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT', 'CacheControl': 'max-age=94608000'}
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_IS_GZIPPED = True

AWS_DEFAULT_REGION = AWS_S3_REGION_NAME


# Import local settings

try:
    from .local_settings import *  # noqa: F401, F403
except ImportError:
    pass


# Testing-specific settings

if TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'app-cache-test',
        }
    }
