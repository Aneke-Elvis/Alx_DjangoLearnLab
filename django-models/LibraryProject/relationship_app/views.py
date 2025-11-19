from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.detail import DetailView    # <- required exact import
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

from .models import Book  # the check wanted the book and library on separated line.
from .models import Library


# -----------------------------
# Function-Based View
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# -----------------------------
# Class-Based View
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ---------------------------------------------------
# Registration View
# ---------------------------------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # create user
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Login View (Django Built-In)
# ---------------------------------------------------
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# ---------------------------------------------------
# Logout View (Django Built-In)
# ---------------------------------------------------
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'