# api/urls.py

from django.urls import path
from django.http import JsonResponse

# Temporary root view to confirm API routing works.
def ping(request):
    return JsonResponse({'status': 'ok', 'message': 'api is up'})

urlpatterns = [
    path('', ping, name='api-root'),
]
