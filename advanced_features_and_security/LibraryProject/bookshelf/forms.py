from django import forms
from .models import Book



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_year', 'author', 'category']


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_year', 'author', 'category']