from django.views import View
from django.shortcuts import redirect
from django.conf import settings
from django.shortcuts import render
from .models import Menu, MasterChef
from order.models import Order, OrderItem
from .forms import QueryForm, BookATableForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    master_chefs = MasterChef.objects.all()
    return render(request, 'about.html', {"chefs": master_chefs})


@login_required(login_url="login")
def menu(request):
    menu = Menu.objects.all()
    order, Created = Order.objects.get_or_create(
        customer=request.user, completed=False)
    order_item = OrderItem.objects.filter(
        Q(order=order) & Q(order_id__completed=False)).all()

    items = []

    for i in order_item:
        items.append(i.product.pk)

    return render(request, 'menu.html', {
        'menu': menu,
        'order_item': order_item,
        'items': items

    })


def contact(request):
    form = QueryForm()
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!")
        else:
            messages.error(request, "Invalid")
    return render(request, 'contact.html', {"form": form})


def booking(request):
    form = BookATableForm()
    if request.method == "POST":
        form = BookATableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!")
        else:
            messages.error(request, "Invalid")

    return render(request, 'booking.html', {'form': form})
