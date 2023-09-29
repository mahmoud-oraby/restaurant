from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
# Create your views here.


class RegisterView(View):
    """
    A view for user registration.

    Allows users to register on the website using a form.
    Upon successful registration, the user is logged in
    and a welcome email is sent to their registered email address.
    """
    template_name = "html/register.html"

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to the registration page.

        If the user is already authenticated, redirect them
        to the main index page. Otherwise, instantiate a new
        user registration form and render the registration page.
        """
        if request.user.is_authenticated:
            return redirect("main:index")
        else:
            form = NewUserForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user registration.

        Process the submitted registration form. If the form
        is valid, save the user, log them in, send a welcome
        email, and redirect them to the login page. If the form
        is invalid, render the registration page with the form
        and display validation errors.
        """
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            subject = 'Welcome to our website.'
            message = 'Welcome, Thanks for register to our site.'
            to_email = request.user.email
            send_mail(subject, message, from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[to_email], fail_silently=True)
            return redirect('login')
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    """
    Handle user login.

    If the request method is GET:
        - If the user is already authenticated, redirect them to the main index page.
    If the request method is POST:
        - Validate the submitted login form.
        - If the form is valid, authenticate the user, log them in,
          display a success message, and redirect them to the main index page.
        - If the form is invalid, display an error message.
    In all other cases:
        - Display the login form.
    """
    template_name = "html/login.html"

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        if request.user.is_authenticated:
            return redirect("main:index")
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:index")
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

        return render(request, self.template_name, {"form": form})


def sign_out(request):
    """
    Handle user logout.

    Log the user out, display a success message, and redirect them to the login page.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")
