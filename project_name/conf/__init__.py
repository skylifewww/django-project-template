from .models import Config


class LazyConfig(object):
    _config = Config

    def __getattr__(self, name):
        return getattr(self._config.get_solo(), name)

    def __str__(self):
        return str(self._config.get_solo())

config = LazyConfig()
