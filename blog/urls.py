from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('about/<int:pk>/', views.AboutDetail.as_view(), name='about'),
]
