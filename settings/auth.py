AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/signin/'
LOGIN_ERROR_URL = '/signin/failed/'

AUTH_USER_MODEL = 'users.User'
