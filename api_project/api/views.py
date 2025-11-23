# api/views.py

from rest_framework import generics  # <- must import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  # <- must extend generics.ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
