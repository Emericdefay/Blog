"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
from typing import cast
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cast(str, os.getenv('DJANGO_SECRET_KEY', 'replace-me'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True').lower() in ('True', '1', 'true')
ALLOWED_HOSTS = [
    '.blog-korpo.azurewebsites.net',
    '.emericdefay.com',
    '127.0.0.1',
    '1.1.1.1',
    'localhost',
]

CSRF_TRUSTED_ORIGINS=[
    'https://emericdefay.com',
    'https://*.emericdefay.com',
    'https://*.blog-korpo.azurewebsites.net',
]

CORS_ALLOWED_ORIGINS = [
    "https://emericdefay.com",
    "https://*.emericdefay.com",
    "https://blog-korpo.azurewebsites.net",
    "https://*.blog-korpo.azurewebsites.net",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


# Application definition

INSTALLED_APPS = [
    'posts',
    'contact',
    'resume',

    'mdeditor',
    'crispy_forms',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    #'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# If you are using different databases for development and production.

# if not DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': cast(str, os.getenv('DB_NAME')),
#             'USER': cast(str, os.getenv('DB_USER')),
#             'PASSWORD': cast(str, os.getenv('DB_PASSWORD')),
#             'HOST': cast(str, os.getenv('DB_HOST')),
#             'PORT': int(cast(int, os.getenv('DB_PORT')))
#         }
#     }
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=cast(str, os.getenv('SENTRY_KEY')),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
STATIC_URL = cast(str, os.getenv('STATIC_URL', '/static/'))
MEDIA_URL = cast(str, os.getenv('MEDIA_URL', '/media/'))
STATIC_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    cast(str, os.getenv('STATIC_DIRS', os.path.join(BASE_DIR, 'static'))),
    os.path.join(BASE_DIR, 'posts', 'static'),
    '/var/www/static'
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
#STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage') # CompressedManifestStaticFilesStorage


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# mdeditor
X_FRAME_OPTIONS = 'SAMEORIGIN'

MDEDITOR_CONFIGS = {
    'default': {
        'lineWrapping': True,
        'language': 'en',
    },
}

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


if not DEBUG:
    #STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    #MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    #STATIC_ROOT = os.path.join(BASE_DIR, 'posts', 'static')
    #MEDIA_ROOT = os.path.join(BASE_DIR, 'posts', 'media')
    #STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    #MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_ROOT = cast(str, os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'staticfiles')))
    MEDIA_ROOT  = cast(str, os.getenv('MEDIA_ROOT' , os.path.join(BASE_DIR, 'media'      )))
    pass
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'posts', 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'posts', 'media')

COMMENT_FLAGS_ALLOWED = 3

COMMENT_SHOW_FLAGGED = True

COMMENT_FLAG_REASONS = [
    (1, ('Spam | Existe uniquement pour promouvoir un service')),
    (2, ('Abusif | Haine gratuite')),
    (3, ('Raciste | Maladie mentale')),
]

COMMENT_ALLOW_ANONYMOUS = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800

# EMAIL SERVICE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = cast(str, os.getenv('DEFAULT_FROM_EMAIL', 'replace-me'))
EMAIL_HOST = cast(str, os.getenv('EMAIL_HOST', 'replace-me'))
EMAIL_HOST_USER = cast(str, os.getenv('EMAIL_HOST_USER', 'replace-me'))
EMAIL_HOST_PASSWORD = cast(str, os.getenv('EMAIL_HOST_PASSWORD', 'replace-me'))
EMAIL_PORT = int(cast(int, os.getenv('EMAIL_PORT', '123')))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False').lower() in ('True', '1', 'true')
