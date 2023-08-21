from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=20,error_messages={
        "required":"Your username must not be empty",
        "max_length":"Please enter a shorter name"
    })
    email = forms.EmailField(max_length=255,error_messages={
        "max_length":"Please enter a shorter email"
    })

    class Meta:
        model = User
        fields = ('username','email','password1','password2')