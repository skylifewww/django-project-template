from jinja2 import Environment

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils.timezone import now

from {{ project_name }}.conf import config
from {{ project_name }}.core.utils import intspace, set_param


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'dir': dir, 'list': list, 'len': len, 'enumerate': enumerate, 'range': range,
        'settings': settings, 'config': config,
        'now': now, 'intspace': intspace, 'set_param': set_param,
        'static': staticfiles_storage.url, 'url': reverse,
    })
    return env
