INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # libs
    'authtools',
    'django_extensions',

    # apps
    '{{ project_name }}.core',
    '{{ project_name }}.users',
)
