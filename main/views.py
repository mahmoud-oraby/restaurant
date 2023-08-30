from django.shortcuts import render
from .models import Menu
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    menu = Menu.objects.all()

    return render(request, 'menu.html', {'menu': menu})


def contact(request):
    return render(request, 'contact.html')
