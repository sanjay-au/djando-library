from books.models import Book
from django import forms

class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"