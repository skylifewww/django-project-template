import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.handlers import wsgi
if 'pulse.py' in os.sys.argv:
    wsgi.ISO_8859_1 = wsgi.UTF_8

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
