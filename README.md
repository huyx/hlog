# Django 项目模板

创建一个自己使用的 Django 项目模板。

## 任务

* [x] 使用新的目录结构
  * [x] 所有应用放到 `apps` 目录
* [x] 所有文件使用 UTF-8 编码，使用 `\n` 作为行分隔符
* [x] 修改默认配置，适合中国
* [x] 使用 `django-environ` 重构配置文件
* [x] 使用 `django-extensions`
* [x] 使用 `django-debug-toolbar`
* [x] 添加应用 `apps.core`
  * [x] `app.core.context_processors.app_versions` - 显示所有 apps 的版本

## 项目布局

* `<project>`
  * `<static>`
  * `<templates>`
    * `404.html`
    * `500.html`
    * `base.html`
  * `__init__.py`
  * `settings.py`
  * `urls.py`
  * `wsgi.py`
* `<apps>`
  * `<core>`
    * `<migrations>`
      * `__init__.py`
      * `admin.py`
      * `apps.py`
      * `context_processors.py`
      * `models.py`
      * `tests.py`
      * `views.py`
  * `__init__.py`
* `.env`
* `manage.py`
* `requirements.txt`

## 用法

```
django-admin startproject --template=https://github.com/huyx/django-project-template/archive/master.zip project_name
```

## .env 文件

参考： http://django-environ.readthedocs.io

注意事项:

* 环境变量名允许字母、数字、下划线
* 严格符合 `ENVIRON_VARIABLE_NAME=VALUE` 的行才生效，`=` 左边不能有空格
* 不符规范的行会静悄悄的忽略掉，因此可用作注释行

示例，参见 .env 文件
