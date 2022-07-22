"""
Django settings for youthmarket project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable"
        raise ImproperlyConfigured(error_msg)
# heroku배포 참고: https://eunjin3786.tistory.com/244
# SECRET_KEY = get_secret("SECRET_KEY")
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', "django-insecure-ageps9g1*oesnqqs@93q!8fvxruzpyvl--+bp$ysme$a*fm%qd")
# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True
DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'channels',
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa',
    'post',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'youthmarket.urls'

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

WSGI_APPLICATION = 'youthmarket.wsgi.application'
ASGI_APPLICATION = 'youthmarket.routing.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True
# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ICON_72_PATH = 'http://127.0.0.1:8000/media/icons/icon_72x72.png'
ICON_96_PATH = 'http://127.0.0.1:8000/media/icons/icon_96x96.png'
ICON_128_PATH = 'http://127.0.0.1:8000/media/icons/icon_128x128.png'
ICON_144_PATH = 'http://127.0.0.1:8000/media/icons/icon_144x144.png'
# ICON_144_PATH = os.path.join(BASE_DIR, 'static\images\icons', 'icon-144x144.png')
# ICON_144_PATH = os.path.join('C:\\Users\\kyung\\Desktop\\test3\\youthmarket\\static\\images\\icons', 'icon-144x144.png')

ICON_152_PATH = 'http://127.0.0.1:8000/media/icons/icon_152x152.png'
ICON_192_PATH = 'http://127.0.0.1:8000/media/icons/icon_192x192.png'
ICON_384_PATH = 'http://127.0.0.1:8000/media/icons/icon_384x384.png'
ICON_512_PATH = 'http://127.0.0.1:8000/media/icons/icon_512x512.png'
# ICON_512_PATH = os.path.join(BASE_DIR, 'static\images\icons', 'icon-512x512.png')
ICON_PATH = 'http://127.0.0.1:8000/media/icons/icon.PNG'
PWA_APP_NAME = 'youthmarket'
PWA_APP_DESCRIPTION = "youthmarket"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
# PWA_APP_PREFER_RELATED_APPLICATIONS = True # https://web.dev/i18n/ko/installable-manifest/
PWA_APP_ICONS = [
	{
		'src': ICON_72_PATH,
		'sizes': '72x72',
        'type': 'image/png',
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_96_PATH,
		'sizes': '96x96',
        'type': 'image/png',
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_128_PATH,
		'sizes': '128x128',
        'type': 'image/png',
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_144_PATH,
        # 'src': "C:\\Users\\kyung\\Desktop\\test3\\youthmarket\\static\\images\\icons\\icon-144x144.png",
		'sizes': '144x144',
        'type': 'image/png',
        # 'purpose': 'any maskable'
        'purpose': 'maskable'
	},
    {
		'src': ICON_152_PATH,
		'sizes': '152x152',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_128_PATH,
		'sizes': '192x192',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_192_PATH,
		'sizes': '192x192',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_384_PATH,
		'sizes': '384x384',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_512_PATH,
		'sizes': '512x512',
        'type': 'image/png',
        'purpose': 'maskable'
	}

]
PWA_APP_ICONS_APPLE = [
	{
		'src': ICON_72_PATH,
		'sizes': '72x72',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_96_PATH,
		'sizes': '96x96',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_128_PATH,
		'sizes': '128x128',
        'type': 'image/png'
        # 'purpose': 'any maskable'
	},
    {
		'src': ICON_144_PATH,
        # 'src': "C:\\Users\\kyung\\Desktop\\test3\\youthmarket\\static\\images\\icons\\icon-144x144.png",
		'sizes': '144x144',
        'type': 'image/png',
        # 'purpose': 'any maskable'
        'purpose': 'maskable'
	},
    {
		'src': ICON_152_PATH,
		'sizes': '152x152',
        'type': 'image/png'
	},
    {
		'src': ICON_192_PATH,
		'sizes': '192x192',
        'type': 'image/png'
	},
    {
		'src': ICON_384_PATH,
		'sizes': '384x384',
        'type': 'image/png'
	},
    {
		'src': ICON_512_PATH,
		'sizes': '512x512',
        'type': 'image/png',
        # 'purpose': 'any maskable'
        'purpose': 'maskable'
	}
]
PWA_APP_SPLASH_SCREEN = [
	{
		'src': ICON_PATH,
		'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
	}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
# 아래 처럼 바꾸면 Redis안쓰고 just InMemory DB만 사용
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }
