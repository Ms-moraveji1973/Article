from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import Article , Category
# Create your views here.

class ArticleList(ListView):
    model = Article
    paginate_by = 1
    template_name = 'artilce/article_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleList , self).get_context_data()
        context['articles'] = Article.objects.published()
        context['category'] = Category.objects.published()
        return context



class ArticleDetail(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = 'detail'

def category(request , slug):
    context = {
        "category" : get_object_or_404(Category, slug=slug , status=True)
    }
    return render(request , "article/category.html" , context)