from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.detail import DetailView    # <- required exact import
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test

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

# Helper role-check functions
def is_admin(user):
    try:
        return user.is_authenticated and user.userprofile.role == 'Admin'
    except Exception:
        return False

def is_librarian(user):
    try:
        return user.is_authenticated and user.userprofile.role == 'Librarian'
    except Exception:
        return False

def is_member(user):
    try:
        return user.is_authenticated and user.userprofile.role == 'Member'
    except Exception:
        return False


# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    # add context/data for admins here
    context = {'title': 'Admin Dashboard'}
    return render(request, 'relationship_app/admin_view.html', context)


# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    # add context/data for librarians here
    context = {'title': 'Librarian Dashboard'}
    return render(request, 'relationship_app/librarian_view.html', context)


# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    # add context/data for members here
    context = {'title': 'Member Area'}
    return render(request, 'relationship_app/member_view.html', context)