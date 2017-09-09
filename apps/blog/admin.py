from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models


@admin.register(models.Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'order', 'tags')
    radio_fields = {
        'status': admin.HORIZONTAL,
        'order': admin.HORIZONTAL,
    }
