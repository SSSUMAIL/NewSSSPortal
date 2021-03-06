"""
Django settings for News_Portal_proj project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f$kg8e84-px2*^z)&$_90_o--!$&fjwla*s@!#3*ojqa#-&uq1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainApp.apps.MainappConfig',

    'widget_tweaks',
    'user',

    'django_apscheduler',

    # apps requiered for allauth:
    'django.contrib.sites',

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',

    'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.facebook',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'News_Portal_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mainApp/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'News_Portal_proj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMINS = [
    ('admin', 'alex.kononuk88@gmail.com'),
]
SERVER_EMAIL = 'notificator@mail.com'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {
    'signup': 'user.models.BasicSignupForm',
}
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mccuyper'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@gmail.com'
EMAIL_HOST_PASSWORD = 'xbct wvgn rfaz znht'

# This is a Django app that adds a lightweight wrapper around APScheduler. 
# It enables storing persistent jobs in the database using Django's ORM.
# https://github.com/jcass77/django-apscheduler
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

# LOGIN_URL = '/user/login/'
# AUTH_USER_MODEL = "user.User"

#
# CELERY_BROKER_URL ??? ?????????????????? ???? URL ?????????????? ??????????????????(Redis).
# ???? ?????????????????? ???? ?????????????????? ???? ?????????? 6379.
CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND ??? ?????????????????? ???? ?????????????????? ?????????????????????? ????????????????????
# ??????????.
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT ??? ???????????????????? ???????????? ????????????.
CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER ??? ?????????? ???????????????????????? ??????????.
CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER ??? ?????????? ???????????????????????? ??????????????????????.
CELERY_RESULT_SERIALIZER = 'json'

INTERNAL_IPS = [
    '127.0.0.1',
]

CACHES = {
    'default': {
        'TIMEOUT': 60,
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'verbose'
        },
        'errors': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'database_queries': {
            'class': 'logging.FileHandler',
            'filename': 'db.log'
        },
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        # logs for live server
        'django': {
            'handlers': ['console', 'general'],
            'propagate': True,
        },
        # logs for 5xx and 4xx errors
        'django.request': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        # logs for db queries
        'django.db.backends': {
            'handlers': ['database_queries'],
            'level': 'DEBUG'
        },
        'myproject.custom': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
    'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
}

