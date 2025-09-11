from .base import env

DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases 
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
        'OPTIONS': {
            'options': "-c search_path=public"
        },
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
    },
}

CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE")
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE")
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT")
