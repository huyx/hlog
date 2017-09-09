from django.contrib.postgres.fields.array import ArrayField
from django.db import models


class Post(models.Model):
    STATUS_DRAFT = 'D'
    STATUS_PUBLISHED = 'P'
    STATUS_PRIVATE = 'I'

    STATUS_CHOICES = (
        (STATUS_DRAFT, '草稿'),
        (STATUS_PUBLISHED, '已发布'),
        (STATUS_PRIVATE, '私密'),
    )

    TOP_CHOICES = zip(range(3, -4, -1), map(str, range(3, -4, -1)))

    title = models.CharField('标题', max_length=200)
    content = models.TextField('正文')
    abstract = models.CharField('摘要', max_length=250)
    status = models.CharField('状态', max_length=1, default=STATUS_PUBLISHED, choices=STATUS_CHOICES)
    order = models.PositiveSmallIntegerField('排序', default=0, choices=TOP_CHOICES)
    tags = ArrayField(models.CharField(max_length=20), size=10, verbose_name='标签')
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    updata_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-order', '-create_at']
