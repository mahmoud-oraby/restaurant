from django import forms
from .models import Query, BookATable
from django.utils import timezone


class QueryForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Subject...."}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2, 'placeholder': "Message...."}))

    class Meta:
        model = Query
        fields = ['name', 'email', 'subject', 'message']


class BookATableForm(forms.ModelForm):
    NUM_PEOPLE = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five"),
    )
    date = forms.DateTimeField(label="Date & Time",
                               input_formats=['%Y-%m-%d %H:%M'],
                               widget=forms.DateTimeInput(
                                   attrs={'type': 'datetime-local'}),
                               initial=timezone.now().strftime('%Y-%m-%d %H:%M'))

    num_people = forms.ChoiceField(label="No of people", choices=NUM_PEOPLE)

    class Meta:
        model = BookATable
        fields = ['name', 'email', 'date', 'num_people', 'special_request']
