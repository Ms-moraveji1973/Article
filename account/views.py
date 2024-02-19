from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article
from .mixins import FieldMixin , FormValidMixin ,AuthorAccessMixin ,SuperUserMixin

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

class ArticleCreate(LoginRequiredMixin,FormValidMixin,FieldMixin, CreateView):
    model = Article
    template_name = "registration/article_create_update.html"
    
class ArticleUpdate(AuthorAccessMixin,FormValidMixin,FieldMixin, UpdateView):
    model = Article
    template_name = "registration/article_create_update.html"

class ArticleDelete(SuperUserMixin , DeleteView):
    model = Article
    template_name = "registration/article_delete.html"
    success_url = reverse_lazy('home')