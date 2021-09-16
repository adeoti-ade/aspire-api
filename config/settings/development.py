from .base import *

import os

DEBUG = True
ALLOWED_HOSTS = config('ALLOWED_HOSTS', ['*'])
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
