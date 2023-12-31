from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
]
