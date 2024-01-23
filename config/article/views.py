from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
# Create your views here.

class ArticleList(ListView):
    model = Article
    template_name = 'artilce/article_list.html'
    context_object_name = 'articles'