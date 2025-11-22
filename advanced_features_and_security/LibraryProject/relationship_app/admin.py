# relationship_app/admin.py
from django.contrib import admin
from .models import (
    Author, Library, Book, UserProfile, Librarian
)

admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Librarian)
