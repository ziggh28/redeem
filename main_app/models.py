from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  comment = models.TextField(max_length=250)
 

def __str__(self):
    return self.name

def get_absolute_url(self):
  return reverse('posts_detail', kwargs={'post_id': self.id})
