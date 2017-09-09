def make_permission_name_better(sender, **kwargs):
    """Django 缺省的 Permission 中的 name 实在是不符合中国人的习惯，改进一下
    """
    from django.contrib.auth.models import Permission

    for permission in Permission.objects.all():
        if permission.name.startswith('Can add'):
            permission.name = '添加'
        elif permission.name.startswith('Can change'):
            permission.name = '修改'
        elif permission.name.startswith('Can delete'):
            permission.name = '删除'
        permission.save()
