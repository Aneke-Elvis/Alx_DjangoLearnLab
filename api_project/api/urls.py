# api/urls.py

from django.urls import path
from django.http import JsonResponse
from .views import BookList

# Temporary root view to confirm API routing works.
def ping(request):
    return JsonResponse({'status': 'ok', 'message': 'api is up'})

urlpatterns = [
    path('', ping, name='api-root'),
    path('books/', BookList.as_view(), name='book-list'),
]
