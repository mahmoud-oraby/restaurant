from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UniqueEmail(forms.EmailField):
    def validate(self, value):
        super().validate(value)
        if User.objects.filter(email=value).exists():
            raise ValidationError("This email is already exists.")
        

class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=20,error_messages={
        "required":"Your username must not be empty",
        "max_length":"Please enter a shorter name"
    })
    email = UniqueEmail(max_length=255,error_messages={
        "max_length":"Please enter a shorter email"
    })
    

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    