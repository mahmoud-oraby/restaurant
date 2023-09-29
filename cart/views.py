from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from order.models import Order, OrderItem
from django.views.generic import DeleteView
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy

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


class RemoveItemFromCartView(DeleteView):
    model = OrderItem
    success_url = reverse_lazy("cart:cart")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
