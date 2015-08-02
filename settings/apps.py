INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # libs
    'django_extensions',
    'djangobower',
    'solo',
    'pulsar.apps.pulse',

    # apps
    '{{ project_name }}.conf',
    '{{ project_name }}.core',
    '{{ project_name }}.users',
)
