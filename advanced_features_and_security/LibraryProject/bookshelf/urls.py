from django.urls import path
from . import views
from .views import example_form_view

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_create, name='book_create'),
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path("example-form/", example_form_view, name="example_form"),
]
