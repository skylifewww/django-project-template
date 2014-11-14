from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from django.test.utils import override_settings


@override_settings(CELERY_ALWAYS_EAGER=True, BROKER_BACKEND='memory')
class TestCase(SimpleTestCase):
    fixtures = []

    def reverse(self, *args, **kwargs):
        return reverse(*args, **kwargs)
