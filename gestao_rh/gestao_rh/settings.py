

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 't@-&svr*4xfezln^6zqv=+3lnzft859+wmf&n6ev1s0(alt393'

DEBUG = True

ALLOWED_HOSTS = ['18.231.180.250']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.empresas',
    'apps.funcionarios',
    'apps.departamentos',
    'apps.documentos',
    'apps.registro_hora_extra',
    'apps.core',
    'bootstrapform',
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

ROOT_URLCONF = 'gestao_rh.urls'

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

WSGI_APPLICATION = 'gestao_rh.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# copreendendo arquivos staticos Aula 31
# Esse altera o nome lá no html, par ao caminho da pasta
STATIC_URL = '/static/'

# Esse indica os caminhos por onde o python deve buscar
# os arquivos staticos, pode está em qualquer lugar do servidor.
# caminho abisoluto = '/var/www/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# ----------------
# Vai apontar a pasta root que vai concentrar dos arquivos
# staticos na hora de fazer o deploy
# Vai ser usando pelo comando python manage.py collectstatic
# Vai percorrer todas as pastas no SATATICFILES_DIRS
# Vai copiar os arquivos e vai setar em uma pasta raíz com o nome static dado pelo STATIC_ROOT
#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# --------------------


LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = '/accounts/login'
##############

# Vamos usar essa local, por enquanto.
MEDIA_URL = '/media/'


# Em empresa grande há uma máquina sepadara que aponta para esse servidor de arquivos.
# NO caso em uma pasta compartilhada. Com isso, de vez de passar o BASE_DIR ... pode passar
# o caminho absoluto da pasta de rede
# exemplo | MEDIA_ROOT = caminho/da/pasta/servidor

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Outra forma comum é manter os arquivos staticos na nuvem.
# Nos próximos capítulos colocar no S3 da Amazon.
# TEm o serviço do glasian no futuro para guardar arquivos
