from pathlib import Path
from dotenv import load_dotenv

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = "True"

ALLOWED_HOSTS = ["127.0.0.1", "registration-via-telegram.herokuapp.com"]


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# BOT_TOKEN = os.getenv("BOT_TOKEN")
# AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
# AIRTABLE_NAME = os.getenv("AIRTABLE_NAME")
# AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
# DJANGO_DEBUG = "False"
# SECRET_KEY = os.getenv("SECRET_KEY")


BOT_TOKEN = "5532784232:AAE8cfO0FsIo_At4uePg8zvBK9fqv8CPxkU"
AIRTABLE_BASE_ID = "app3vcxFEDlEdStCB"
AIRTABLE_NAME = "django-tgbot"
AIRTABLE_API_KEY = "keyCYj6sE0mNnqoJw"
SECRET_KEY = "django-insecure-x$(t(ke0q=j#i&30q8dm#m^t$6zb&*_75=o4+-#a8ufqp5x7y@"


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tgbot_manage',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RegistrationViaTelegram.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = 'RegistrationViaTelegram.wsgi.application'

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

STATICFILES_DIRS = (BASE_DIR / "static",)

STATIC_ROOT = "staticfiles/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
