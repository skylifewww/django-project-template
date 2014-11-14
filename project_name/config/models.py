from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel


class Config(SingletonModel):
    contacts = models.TextField(_('contacts'))

    class Meta:
        verbose_name = _('settings')
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}'.format(self._meta.verbose_name)
