from django.urls import path

from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('post/', views.post, name='post'),
  path('allpost/', views.posts_index, name='posts_index'),
  path('allpost/<int:post_id>/', views.posts_detail, name="posts_detail"),
  path('posts/create/', views.postCreate.as_view(), name='posts_create'),
]