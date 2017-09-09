# hlog

一个简单的博客项目

特色：

* 用 PostgreSQL 作为数据库: tag 变得如此简单
* 编辑器采用 django-summernote: 没有依赖包，清爽

参考：

* https://github.com/liangliangyy/DjangoBlog
* https://djangopackages.org/grids/g/wysiwyg/


## 任务

* [x] 模型设计
  * Post(title, content, abstract, top, status, tags, create_at, update_at)
* [ ] 页面设计
  * [ ] 首页
  * [ ] 列表页
  * [ ] 详细页
  * [x] 编辑/新建(admin?) - 用 admin 页面
* [x] 后台管理页面采用 WSIWYG 编辑器
