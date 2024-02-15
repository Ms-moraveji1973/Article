from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView , CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article

# Create your views here.
@login_required
def home(request):
    return render(request ,"registration/home.html")


class Home(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"
    
    def get_queryset(self):
        if self.request.user.is_superuser :
            return Article.objects.all()
        else:
            return Article.objects.filter(auther=self.request.user)

class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Article
    fields = ['title','slug' ,'category' ,'description' ,'image' ,'status' ,'auther']
    template_name = "registration/article_create_update.html"