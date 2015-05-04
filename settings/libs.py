from settings.static import rel

# grappelli
GRAPPELLI_ADMIN_TITLE = '{{ project_name }} - Administration panel'

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
