"""
hlog 配置文件, 参考文档

* https://docs.djangoproject.com/en/1.11/topics/settings/
* https://docs.djangoproject.com/en/1.11/ref/settings/
* https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
* https://github.com/joke2k/django-environ
"""

import os

from environ import Env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 读取环境变量，.env 文件采用 utf-8 编码
Env.read_env(open(os.path.join(BASE_DIR, '.env'), encoding='utf-8'))
env = Env()

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

DEBUG = env.bool('DJANGO_DEBUG', True)
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])
SECRET_KEY = env.str('DJANGO_SECRET_KEY', '7=w%b(0@#ojjb6egx7+ba!@rnq-pfs8mrue^-i(wm$gxag3e17')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'bootstrap3',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'project', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.app_versions',
            ],
        },
    },
]

DATABASES = {
    'default': env.db('DJANGO_DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')),
}

# 密码有效性验证
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# 国际化
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = env.str('DJANGO_LANGUAGE_CODE', 'zh-hans')
TIME_ZONE = env.str('DJANGO_TIME_ZONE', 'Asia/Shanghai')
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静态文件 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

_STATIC_DIR = os.path.join(BASE_DIR, 'project', 'static')
os.makedirs(_STATIC_DIR, exist_ok=True)

STATICFILES_DIRS = [
    _STATIC_DIR,
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 配置 django-debug-toolbar
# https://github.com/jazzband/django-debug-toolbar

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = env.list('DJANGO_INTERNAL_IPS', default=['127.0.0.1'])
    DEBUG_TOOLBAR_CONFIG = {
        'JQUERY_URL': 'https://code.jquery.com/jquery-3.2.1.min.js',
    }

# 配置 django-bootstrap3
#
