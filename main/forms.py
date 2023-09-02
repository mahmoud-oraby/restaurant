from django import forms
from .models import Query


class QueryForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Subject...."}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2, 'placeholder': "Message...."}))

    class Meta:
        model = Query
        fields = ['name', 'email', 'subject', 'message']
