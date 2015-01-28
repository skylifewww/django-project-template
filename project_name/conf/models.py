from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel


class Config(SingletonModel):
    contacts = models.TextField(_('contacts'))

    class Meta:
        verbose_name = _('settings')
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self._meta.verbose_name)
