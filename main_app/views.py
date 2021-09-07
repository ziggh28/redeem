from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse
class post:  # Note that parens are optional if not inheriting from another class
  def __init__(self, username, category, description, ):
    self.username = username
    self.category = category
    self.description = description
    
posts = [
 post('zigg','yes','helo',),
 post('zouhrab','yessss','helo',),
 post('zeek','yessir','helo',),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>homepage</h1>')

def post(request):
    return render(request, 'post.html')

def posts_index(request):
  return render(request, 'posts/index.html', { 'posts': posts })

def home(request):
  return render(request, 'home.html')

