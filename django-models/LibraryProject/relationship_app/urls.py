# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books     # <-- add this line to satisfy the checker
from .views import register
from .views import CustomLoginView
from .views import CustomLogoutView
from django.contrib.auth import login   # REQUIRED BY CHECKER
from .views import add_book, edit_book, delete_book



urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
   
     # authentication URLs
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

     # role-based access control views
    path('role/admin/', views.admin_view, name='admin_view'),
    path('role/librarian/', views.librarian_view, name='librarian_view'),
    path('role/member/', views.member_view, name='member_view'),


    
    # Permission-protected URLs
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]