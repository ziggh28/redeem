from django.urls import path, include

from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('posts/', views.posts_index, name='posts_index'),
  path('allpost/<int:post_id>/', views.posts_detail, name="post_detail"),
  path('posts/create/', views.postCreate.as_view(), name='post_create'),
  path('posts/<int:pk>/update/', views.postUpdate.as_view(), name='post_update'),
  path('posts/<int:pk>/delete/', views.postDelete.as_view(), name='post_delete'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('login/', views.Login.as_view(), name='login'), 
  path('accounts/signup/', views.signup, name="signup"),
]