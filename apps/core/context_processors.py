from collections import OrderedDict

import django
from django.apps import apps

UNKNOWN = '<UNKNOWN>'


def _get_app_version(app_config):
    if hasattr(app_config, 'version'):
        return app_config.version

    app_module = app_config.module

    if hasattr(app_module, '__version__'):
        return str(app_module.__version__)
    if hasattr(app_module, 'VERSION'):
        return str(app_module.VERSION)

    return UNKNOWN


def app_versions(request):
    app_versions = OrderedDict()
    app_versions['django'] = django.__version__

    for app_config in apps.app_configs.values():
        # 跳过 django 自带的 apps
        if app_config.module.__name__.partition('.')[0] == 'django':
            app_versions[app_config.module.__name__] = None
        else:
            app_versions[app_config.module.__name__] = _get_app_version(app_config)

    return {
        'app_versions': app_versions
    }
