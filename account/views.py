from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    return render(request ,"registration/home.html")


class Home(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"
    