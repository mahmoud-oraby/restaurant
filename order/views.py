from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Order, OrderItem
from main.models import Menu
# Create your views here.


def create_order(request, id):
    order, Created = Order.objects.get_or_create(customer=request.user)
    product = Menu.objects.get(id=id)
    order_item, Created = OrderItem.objects.get_or_create(
        product=product, order=order)

    return HttpResponseRedirect(reverse('main:menu'))
