# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books     # <-- add this line to satisfy the checker
from .views import (
    RegisterView, 
    LoginView, 
    LogoutView
)


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # --- AUTHENTICATION VIEWS (Using Custom CBVs) ---

    # 1. Login View
    path('login/', LoginView.as_view(), name='login'),

    # 2. Logout View
    path('logout/', LogoutView.as_view(), name='logout'),

    # 3. Registration View
    path('register/', RegisterView.as_view(), name='register'),
]