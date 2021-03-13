from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from . import api
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'blog'

urlpatterns=[
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='show'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('new/', PostCreateView.as_view(), name='create'),
    path('about/', views.about, name = 'blog-about'),
    path('categories/<slug:slug>/', views.cat_posts, name='cat_posts'),

    path('category/api/', api.category_list),
    path('category/api/<int:pk>/', api.category_detail),
    path('post/api/', api.post_list),
    path('post/api/<int:pk>/', api.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)