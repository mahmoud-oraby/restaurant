from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate,login as auth_login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           auth_login(request,user)
           subject = 'Welcome to our website.'
           message = 'Welcome, Thanks for register to our site.'
           to_email = request.user.email
           send_mail(subject, message,from_email= settings.EMAIL_HOST_USER, recipient_list=[to_email], fail_silently=True)
           return redirect('done')
    else:
        form = NewUserForm()


    return render(request,"html/register.html",{"form":form})


