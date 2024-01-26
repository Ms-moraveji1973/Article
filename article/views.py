from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Article
# Create your views here.

class ArticleList(ListView):
    model = Article
    paginate_by = 1
    template_name = 'artilce/article_list.html'
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = 'detail'