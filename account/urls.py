from django.urls import path
from django.contrib.auth import views
from .views import (
    ArticleDelete,
    Home ,
    ArticleCreate ,
    ArticleUpdate ,
    ArticleDelete ,
    Profile ,
                    )

app_name = 'account'
urlpatterns = [
    path('home' , Home.as_view() , name='home') ,
    path('article/create' , ArticleCreate.as_view() , name="article_create" ) , 
    path('article/update/<int:pk>' , ArticleUpdate.as_view() , name="article_update" ) , 
    path('article/delete/<int:pk>' , ArticleDelete.as_view() , name="article_delete" ) , 
    path('profile/' , Profile.as_view() , name="profile" ) , 
]
