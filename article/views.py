from django.shortcuts import render , get_object_or_404
from django.views.generic import View ,ListView , DetailView
from account.models import User
from .models import Article , Category
# Create your views here.

class ArticleList(ListView):
    paginate_by = 4
    model = Article
    template_name = 'artilce/article_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleList , self).get_context_data()
        context['articles'] = Article.objects.published()
        context['category'] = Category.objects.filter(status=True)
        return context



class ArticleDetail(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = 'detail'
    
    
    
# function base view for category
def category(request , slug):
    context = {
        "category" : get_object_or_404(Category, slug=slug , status=True)
    }
    return render(request , "article/category_list.html" , context)


# class base view for category
class CategoryList(ListView):
    paginate_by = 2
    template_name = "article/category_list.html"
        
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all() , slug=slug)
        return category.articles_cat.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
        
class AuthorList(ListView):
    paginate_by = 2
    template_name = "article/author_list.html"
        
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)
        return author.articles_cat.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
        