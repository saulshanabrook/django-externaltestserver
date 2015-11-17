import os

import dj_database_url

ROOT_URLCONF = "items.urls"
DATABASES = {'default': dj_database_url.config()}
DEBUG = TEMPLATE_DEBUG = True

EXTERNAL_TEST_SERVER = os.environ.get('EXTERNAL_TEST_SERVER', None)

INSTALLED_APPS = (
    "django.contrib.staticfiles",

    "externaltestserver",

    "items",
)
SECRET_KEY = "_"
STATIC_URL = '/static/'
