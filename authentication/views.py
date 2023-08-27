from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate,login as auth_login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
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


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user=authenticate(username=username, password=password)

            if user is not None:
                auth_login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("done")
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="html/login.html",context={'form':form})


def done(request):
    return render(request,'html/done.html')

