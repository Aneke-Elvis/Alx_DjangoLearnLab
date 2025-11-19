# django-models/LibraryProject/relationship_app/forms.py
from django import forms
from .models import Book

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form based on Django's built-in form.
    This can be extended later but is simple enough for this task.
    """
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author', 'library']