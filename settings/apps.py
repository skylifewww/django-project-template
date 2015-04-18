INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # libs
    'djangobower',
    'solo',

    # apps
    '{{ project_name }}.conf',
    '{{ project_name }}.core',
    '{{ project_name }}.users',
)
