from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login as auth_login
# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           auth_login(request,user)
           return redirect('done')
    else:
        form = NewUserForm()


    return render(request,"html/register.html",{"form":form})

def done(request):
    return render(request,"html/done.html")
