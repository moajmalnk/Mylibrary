from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book_details
        fields = "__all__"


class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = ['name', 'phone', 'gmail']
