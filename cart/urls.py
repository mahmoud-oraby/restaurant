from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('remove/<int:id>/', views.remove_item_form_cart, name='remove-item-form-cart'),
]
