from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.add_basket, name='add_basket')
]

