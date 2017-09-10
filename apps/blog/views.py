from django.views.generic import ListView, DetailView

from .models import Article


class HomeView(ListView):
    template_name = 'blog/home.html'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.article_list(self.request)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    paginate_by = 50

    def get_queryset(self):
        return Article.objects.article_list(self.request)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
