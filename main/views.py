from django.shortcuts import render
from .models import Menu, MasterChef
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
    return render(request, 'contact.html')
