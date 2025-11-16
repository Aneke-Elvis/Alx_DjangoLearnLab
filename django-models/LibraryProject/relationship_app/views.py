from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.detail import DetailView    # <- required exact import
from django.views import View # <-- For custom Register, Login, Logout CBVs
from django.contrib.auth import login, logout, authenticate # <-- Auth functions
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm # <-- Login form
from django.conf import settings # <-- Used for redirect URL
from django.urls import reverse_lazy # <-- Used for redirect URL

from .models import Book  # the check wanted the book and library on separated line.
from .models import Library
from .forms import CustomUserCreationForm # <-- Import the form you created
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

# -----------------------------
# Class-Based Views (Authentication)
# -----------------------------

class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'relationship_app/register.html'
    
    def get(self, request):
        """Handle GET requests: Display the empty registration form."""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Handle POST requests: Validate form and create user."""
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the new user in immediately
            login(request, user)
            # Redirect to the success URL defined in settings
            return redirect(settings.LOGIN_REDIRECT_URL) 
            
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'relationship_app/login.html'

    def get(self, request):
        """Handle GET requests: Display the login form."""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Handle POST requests: Authenticate user."""
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the success URL defined in settings
                return redirect(settings.LOGIN_REDIRECT_URL)
        
        # Re-render the form with errors if validation or authentication failed
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        """Handle GET requests: Log user out and redirect."""
        # Logs the user out
        logout(request)
        # Redirect to the URL defined in settings (e.g., login page)
        return redirect(settings.LOGOUT_REDIRECT_URL)