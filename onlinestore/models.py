from django.db import models
from django.contrib.auth.admin import User


class Category(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField()
    description = models.TextField(max_length=2055)
    image = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2055)
    slug=  models.SlugField(unique=True)
    pricce = models.DecimalField(max_digits=4, decimal_places=2,default=0)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default= True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_creator')

    def __str__(self):
        return self.name

    class Meta:
        ordering: ['-updated',]
