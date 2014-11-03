from .settings import *

DEBUG = False

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS']]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')
