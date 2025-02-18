from django.urls import path
from .views import Index,DetailArticleView,LikeArticle,Featured,DeleteArticle,Search,About

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('<int:pk>/',DetailArticleView.as_view(),name="detail_article"),
    path('<int:pk>/like',LikeArticle.as_view(),name="like_article"),
    path('featured-posts/',Featured.as_view(),name="featured"),
    path('<int:pk>/delete/', DeleteArticle.as_view(), name='delete_article'),
    path('search/',Search, name='search'),
    path('about/',About.as_view(), name='about'),
]
