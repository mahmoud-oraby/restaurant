from django import forms
from .models import Profile


class EditInformation(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name',
                  'phone', 'gender', 'country', 'image']
