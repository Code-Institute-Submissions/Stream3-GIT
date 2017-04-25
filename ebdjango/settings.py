import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "False")

ALLOWED_HOSTS = ['ebdjango-test2.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'main',
    'account',
    'django_forms_bootstrap',
    'debug_toolbar',
    'tinymce',
    'emoticons',
    'django.contrib.sites',
    'paypal.standard.ipn',
    'paypal_store',
    'products',
    'threads',
    'polls',
]

DISQUS_WEBSITE_SHORTNAME = 'ebdjango-test2.herokuapp.com'
SITE_ID = 1
DISQUS_API_KEY = os.environ.get("DISQUS_API_KEY", "")
INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ROOT_URLCONF = 'ebdjango.urls'

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

WSGI_APPLICATION = 'ebdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

############ FOR PRODUCTION

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(PROJECT_ROOT, 'static'),
)
#####################################################

############ FOR DEV
"""STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)"""
#####################################################





TEMPLATE_DIRS = (
'ebdjango/ebdjango/templates',
'ebdjango/templates',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Account: to tell Django we want to use this class as our User class
AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.backends.EmailAuth',
)

#TinyMCE settings
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", "js",
                               "tinymce", "tinymce.min.js")
# PayPal Settings
SITE_URL = 'https://ebdjango-test2.herokuapp.com/   '
PAYPAL_NOTIFY_URL = 'https://ebdjango-test2.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'alinechribeiro-facilitator@gmail.com'
PAYPAL_TEST = True