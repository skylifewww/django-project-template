from django.contrib.messages import constants as message_constants

from settings.static import rel

# grappelli
GRAPPELLI_ADMIN_TITLE = '{{ project_name }} - Administration panel'

# jinja2
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jhtml'
# JINJA2_BYTECODE_CACHE_ENABLE = True  # default False
JINJA2_CONSTANTS = {
    'DEFAULT_MESSAGE_LEVELS': message_constants
}

# rest framework
# REST_FRAMEWORK = {
#     'PAGINATE_BY_PARAM': 'limit',
#     'SEARCH_PARAM': 'q'
# }

# bower
BOWER_COMPONENTS_ROOT = rel('public')
BOWER_INSTALLED_APPS = (
    # 'bootstrap#3.2.0',
    # 'jquery#2.1.1',
)

# solo
SOLO_CACHE = 'local'
SOLO_CACHE_TIMEOUT = 60 * 60  # 1 hour
SOLO_CACHE_PREFIX = 'solo'
