from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

app_name = 'blog'

urlpatterns=[
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='show'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('new/', PostCreateView.as_view(), name='create'),
    path('about/', views.about, name = 'blog-about'),
    path('categories/<slug:slug>/', views.cat_posts, name='cat_posts'),
]