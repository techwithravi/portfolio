from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=255)
      # Add this line for category images

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Add this line for post images

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
