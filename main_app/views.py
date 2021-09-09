from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.
# Add the following import
from django.http import HttpResponse
from django.contrib.auth.views import LoginView




# Define the home view
def home(request):
  posts: Post.objects.all()
  return HttpResponse('<h1>homepage</h1>')

def post(request):
  return render(request, 'post.html')


def posts_index(request):
  return render(request, 'posts/index.html', { 'posts': posts })

def home(request):
  return render(request, 'home.html')

def posts_detail(request, post_id):
  posts = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', {'posts': posts})



class postCreate(CreateView):
  
  model = Post
  fields = [ 'title', 'comment']

  
  def form_valid(self,form):
    form.instance.user - self.request.user
    return super().form_valid(form)
  

class postUpdate(UpdateView):
  model = Post 
  fields = [ 'title', 'comment',]

class postDelete(DeleteView):
  model = Post 
   

