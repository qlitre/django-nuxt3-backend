from pathlib import Path
import os

ADMIN_PATH = 'admin'
DEBUG = False
ALLOWED_HOSTS = ['.pythonanywhere.com']

try:
    from .local_settings import *
except ImportError:
    from dotenv import load_dotenv

    load_dotenv(override=False)
    ADMIN_PATH = os.environ.get('ADMIN_PATH')
    HOST_URL = os.environ.get('HOST_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    try:
        ALLOWED_ADMIN = os.environ.get('ALLOWED_ADMIN')
    except AttributeError:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'register.apps.RegisterConfig',  # add
    'blog.apps.BlogConfig',  # add
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # add
    "rest_framework_api_key",  # add
    'mdeditor',  # add
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'project.middleware.AdminProtect',  # add
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'ja'  # change

TIME_ZONE = 'Asia/Tokyo'  # change

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'  # add
MEDIA_URL = '/media/'  # add
MEDIA_ROOT = BASE_DIR / 'media'  # add

"""
add
"""
AUTH_USER_MODEL = 'register.User'

API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"

# mdeditorのおまじない
X_FRAME_OPTIONS = "SAMEORIGIN"

MDEDITOR_CONFIGS = {
    'default': {
        'language': 'en',
        'lineWrapping': True
    }
}

MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.toc',
    'markdown.extensions.tables',
    'markdown.extensions.sane_lists',
    'markdown.extensions.admonition',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.wikilinks',
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
