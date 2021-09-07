from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import post
# Create your views here.
# Add the following import
from django.http import HttpResponse



class Post:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, category, comment, ):
    self.title = title
    self.category = category
    self.comment = comment
    
posts = [
 Post('zigg','yes','helo',),
 Post('zouhrab','yessss','helo',),
 Post('zeek','yessir','helo',),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>homepage</h1>')

def post(request):
    return render(request, 'post.html')

def posts_index(request):
  posts: post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def home(request):
  return render(request, 'home.html')

def posts_detail(request, post_id):
  posts = post.object.get(id=post_id)
  return render(request, 'posts/detail.html', {'posts': posts})

class postCreate(CreateView):
  model = post
  fields = [ 'title', 'category', 'comment',]
  

class postUpdate(UpdateView):
  model = post 
  fields = [ 'title', 'category', 'comment',]

class postDelete(DeleteView):
   model = post 
   success_url = '/posts/'

