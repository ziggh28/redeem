# redeem-it


# redeem it : from the same guys that give you not reddit  
redeem it it's not reddit but we tried . 


## Motivation behind  this 
I was a little embarrassed about my unit 2 project & I wanted to a chance to go back to it fixed some of the mistakes I made. this were the idea for redeem it came from. I wanted see if i improved my skill as developer and if so by how much.   

# screenshots 



![Screen Shot 2021-07-30 at 1 37 19 AM](https://user-images.githubusercontent.com/86076993/127606368-a6faddcf-d6cb-4059-bef8-665390d9c3b1.png)


# trelloboard

https://trello.com/b/ms4i76MJ/redeemit

# technologie Used:


python 

django 

css 

# sample code:

router/posts.js -

```
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
  
    form = UserCreationForm(request.POST)
    if form.is_valid():
      
      user = form.save()
      
      login(request, user)
      return redirect('posts_index')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

```



#what was the biggest chllenge:
apparenty murphy(murphy's law) as a crush on me cause everything goes wrong especially if it's the simple things.   


# what I've learn:
that there's never a one size fits all with code. every problem as unique  own unique answer even if it's the same as catcollector
& im still good at this 



# resources 

https://stackoverflow.com/

https://www.youtube.com/

https://www.geeksforgeeks.org/web-development/?ref=shm


# credit 

instructors 

ben manley - kakashi sensei (sixth hokage)

jurgen steven - naruto uzumaki 

brian krabec - shikamaru nara

carolina urrea - Rock lee  

blake romano - orochimaru



peers 

cory rice - you already know 

cuffy - you still my dawg 

chitra & nick - anub black ops  




honorable mentions  

avis js - biyomon

thank you all 
