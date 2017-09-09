from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .utils import make_permission_name_better


class CoreConfig(AppConfig):
    name = 'apps.core'
    version = '0.1.0'

    def ready(self):
        '''必要的初始化
        '''
        post_migrate.connect(make_permission_name_better, sender=self)
