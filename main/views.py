from django.shortcuts import render
from .models import Menu, MasterChef, Query
from .forms import QueryForm, BookATableForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    master_chefs = MasterChef.objects.all()
    return render(request, 'about.html', {"chefs": master_chefs})


def menu(request):
    menu = Menu.objects.all()

    return render(request, 'menu.html', {'menu': menu})


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
