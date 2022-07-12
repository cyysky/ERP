"""
Django settings for crudexample project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ts@9i_k+dy)d&mk&=-lz$h^%oo==w-l!)0n4um1b$6aw6)wsd9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['sunchonghome.asuscomm.com','localhost','192.168.143.59']#我的设备使用
ALLOWED_HOSTS = ['sunchonghome.asuscomm.com','localhost',]


# Application definition

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media').replace('\\', '/'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'pure_pagination',  # 分頁
    'widget_tweaks', #Forms更改
    
    'ERPSystem',
    'accounts',

    'marketing',
    'production',
    'purchasing',
    'warehouse',

    'demo',
    'calculator',


    #'django_cleanup.apps.CleanupConfig', #new
    #django-allauth必须安装的app
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    #第三方账号相关，根据需求添加
    
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github',
    

]

 # django-allauth相关设置
AUTHENTICATION_BACKENDS = (
      # django admin所使用的用户登录与django-allauth无关
      'django.contrib.auth.backends.ModelBackend',
      # allauth 身份验证
      'allauth.account.auth_backends.AuthenticationBackend',

)
#app django.contrib.sites需要的设置
SITE_ID = 1
# 指定要使用的登录方法(用户名、电子邮件地址两者之一)
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# 要求用户注册时必须填写email
ACCOUNT_EMAIL_REQUIRED = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crudexample.urls'
#ROOT_URLCONF = 'myGallery.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'crudexample.wsgi.application'
 

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'urser': {
        'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': 'postgres_user',
        'PASSWORD': 's3krit'
    },
    'default': {
        'NAME': 'erp',# 資料庫名字
        'ENGINE': 'django.db.backends.mysql',  # 指定使用的資料庫引擎，可以通過 Django.db.backends 來檢視哪些資料庫可以與 Django 配合使用； 
        'USER': "user",  # mysql 使用者名稱稱
        'PASSWORD': '123456',  # 資料庫的密碼
        'HOST': "127.0.0.1",  # 資料庫服務地址， 這裡我們是測試開發 填本地地址 
        'PORT': 3306,   # mysql 對應的埠號 
        'default-character-set': "UTF8",  # 設定編碼規則 utf8
    }
}

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


#LANGUAGE_CODE = 'zh-hans'
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

AUTH_USER_MODEL = "accounts.CustomUser"

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


