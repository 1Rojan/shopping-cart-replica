from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.slug



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:show', kwargs={'pk':self.pk})

