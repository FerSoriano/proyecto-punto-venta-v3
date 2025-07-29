from .base import *  # noqa

# to use the library django-debug-toolbar
INSTALLED_APPS.append("debug_toolbar") # noqa
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware") # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "settings/my.cnf",
        },
    }
}

# to use the library django-debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]
