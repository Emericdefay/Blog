from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'my_database',
    }
} 

LOGGING = {}

STATICFILES_STORAGE = ('whitenoise.storage.CompressedStaticFilesStorage')