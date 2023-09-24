from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from order.models import Order, OrderItem
from main.models import Menu
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def cart(request):
    order = Order.objects.filter(
        Q(customer=request.user) & Q(completed=False)).first()
    order_item = OrderItem.objects.filter(order=order).all()
    if request.method == "POST":
        quantity = int(request.POST.get('quantity'))
        if quantity <= 0:
            messages.error(request, "Should be bigger than 0!")
            return redirect('cart:cart')
        else:
            item_id = request.POST.get('item_id')
            item = OrderItem.objects.get(id=item_id)
            item.quantity = quantity
            item.save()
            order_item = OrderItem.objects.filter(order=order).all()
    total_price = 0
    for item in order_item:
        total_price += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'order_item': order_item,
        'total_price': str(total_price),
    })


def remove_item_form_cart(request, id):
    item = OrderItem.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('cart:cart'))
