from django.urls import path
from .views import ArticleList , ArticleDetail , category , CategoryList
urlpatterns = [
    path('' , ArticleList.as_view() , name="ArticleList" ) , 
    path('<slug:slug>' , ArticleDetail.as_view() , name="ArticleDetail" ),
    path('category/<slug:slug>', CategoryList.as_view() , name="category"),
]