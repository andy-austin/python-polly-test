import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv("DEBUG", True)

SECRET_KEY = 'c(7gxw=$o6n+8)%u*o6@jlg*z$#xuy(3r9u$k_6!1j!wuk$m+'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'drf_yasg',
    'rest_framework',

    'loan.apps.LoanConfig',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request'
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'polly.urls'

WSGI_APPLICATION = 'polly.wsgi.application'

# Django REST Framework configuration
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Swagger configuration for drf-yasg
# https://drf-yasg.readthedocs.io/en/stable/index.html

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': None
}
