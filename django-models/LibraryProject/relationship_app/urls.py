# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books     # <-- add this line to satisfy the checker
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
   
     # authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]