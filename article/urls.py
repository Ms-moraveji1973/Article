from django.urls import path , include
from .views import( 
        ArticleList   ,
        ArticleDetail ,
        ArticlePreview,
        CategoryList  ,
        AuthorList ,
        SearchList
                    )

urlpatterns = [
    path('' , ArticleList.as_view() , name="ArticleList" ) , 
    path('article/<slug:slug>' , ArticleDetail.as_view() , name="ArticleDetail" ),
    path('preview/<int:pk>' , ArticlePreview.as_view() , name="ArticlePreview" ),
    path('category/<slug:slug>', CategoryList.as_view() , name="category"),
    path('author/<slug:username>', AuthorList.as_view() , name="author"),
    #path('author/<slug:username>/page/<int:page>', AuthorList.as_view() , name="author"),
	path('search/', SearchList.as_view(), name="search"),
    path('search/<slug:username>/page/<int:page>', SearchList.as_view() , name="search"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]