from django.urls import path
from .views import ArticleList , ArticleDetail , CategoryList , AuthorList
urlpatterns = [
    path('' , ArticleList.as_view() , name="ArticleList" ) , 
    path('article/<slug:slug>' , ArticleDetail.as_view() , name="ArticleDetail" ),
    path('category/<slug:slug>', CategoryList.as_view() , name="category"),
    path('author/<slug:username>', AuthorList.as_view() , name="author"),
]