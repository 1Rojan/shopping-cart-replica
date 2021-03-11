from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    pass

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}