"""
Django settings for djacket project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import ast


def osenv(env_name):
    """
        Returns an empty string if the required environment
            variable does not exist, else it's value.
    """

    return os.environ.get(env_name, '')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Front-end folder to keep views, styles and scripts.
# Default is set to a BASE_DIR/../'frontend'
FRONTEND_DIR = os.path.join(BASE_DIR, '..', 'frontend')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_pjax',
    'user.apps.UserAppConfig',
    'repository.apps.RepositoryAppConfig',
    'filter.apps.FilterAppConfig'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djacket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(FRONTEND_DIR, 'public', 'build', 'views'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                'easy_pjax.templatetags.pjax_tags'
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djacket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Currently there's not much of a database transaction (only on user/repository creation)
#   so SQLite database would suffice.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/db/djacketdb.sqlite3'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# Static files will be collected to be served in 'BASE_DIR/../static/', outside of server code.

STATIC_URL = '/static/'
STATIC_ROOT = '/srv/static/'
STATICFILES_DIRS = [os.path.join(FRONTEND_DIR, 'public', 'build', 'static'),]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Media files (User avatar images)
# Default is set to ''BASE_DIR/../media', outside of server code.

MEDIA_ROOT = '/srv/media/'
MEDIA_URL = '/media/'


# User authentication urls configuration.

LOGIN_URL = 'index'
LOGOUT_URL = 'user_logout'
LOGIN_REDIRECT_URL = 'index'


# Djacket site name.

SITE_NAME = 'Djacket'


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = osenv('DSCT_KY')


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False if osenv('DJKR_MODE') in ['prod', ''] else True


# For security reasons, set domain or host of your site in ALLOWED_HOSTS
#   e.g.
#       ALLOWED_HOSTS = ['exampledomain.com']
# You can find more details in https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts.

ALLOWED_HOSTS = ['*'] if DEBUG else ast.literal_eval(osenv('DALWD_HSTS'))


# Git repositories deposit folder on server.
#   This is where all the repos will be stored and maintained.

GIT_DEPOSIT_ROOT = '/srv/deposit/'
