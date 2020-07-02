from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,DeletePostView

urlpatterns = [
    #path('',views.home,name='home')
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='post_list'),
    path('post_form/',AddPostView.as_view(),name='post_form'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name='post_delete'),
]