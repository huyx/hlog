"""hlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
]

# 配置: django-debug-toolbar

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar

    # 应该插入到 urlpatterns 最前面
    urlpatterns.insert(0, url(r'^__debug__/', include(debug_toolbar.urls)))

    # 使用 gunicorn 部署测试服务器时，静态文件不能正确返回，需要加上下面的代码
    # 参考文档:
    # * https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#django.contrib.staticfiles.urls.staticfiles_urlpatterns
    # * https://stackoverflow.com/questions/12800862/how-to-make-django-serve-static-files-with-gunicorn/12801140#12801140
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
