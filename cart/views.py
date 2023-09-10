from django.shortcuts import render
from order.models import Order, OrderItem
from main.models import Menu

# Create your views here.


def cart(request):
    order = Order.objects.get(customer=request.user)
    order_item = OrderItem.objects.filter(order=order).all()

    total_price = 0
    for item in order_item:
        total_price += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'order_item': order_item,
        'total_price': str(total_price)
    })
