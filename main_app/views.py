from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.
# Add the following import
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class Login(LoginView):
  template_name = 'login.html'


# Define the home view


def post(request):
  return render(request, 'post.html')


def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', { 'posts': posts })

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', {'post': post})



class postCreate(CreateView):
  
  model = Post
  fields = ['title', 'comment']
  success_url = "/"
  
  def form_valid(self,form):
    print(self.request.user)
    form.instance.user = self.request.user
    return super().form_valid(form)
    
  

class postUpdate(UpdateView):
  model = Post 
  fields = [ 'title', 'comment',]
  success_url = "/"

class postDelete(DeleteView):
  model = Post 
  success_url = "/"


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('posts_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)