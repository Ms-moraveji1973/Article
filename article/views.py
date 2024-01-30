from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Article , Category
# Create your views here.

class ArticleList(ListView):
    model = Article
    paginate_by = 1
    template_name = 'artilce/article_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super(ArticleList , self).get_context_data()
        context['category'] = Category.objects.all()
        return context



class ArticleDetail(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = 'detail'