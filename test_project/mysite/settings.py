import os

ROOT_URLCONF = "items.urls"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '5432',
    }
}
DEBUG = TEMPLATE_DEBUG = True

EXTERNAL_TEST_SERVER = os.environ.get('EXTERNAL_TEST_SERVER', None)

INSTALLED_APPS = (
    "django.contrib.staticfiles",

    "externaltestserver",

    "items",
)
SECRET_KEY = "_"
STATIC_URL = '/static/'
