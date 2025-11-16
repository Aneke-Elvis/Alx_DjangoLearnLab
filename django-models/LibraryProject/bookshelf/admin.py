from django.contrib import admin

from .models import Book # Import the Book model from the current app's models.py

# 1. Define the custom Admin class
class BookAdmin(admin.ModelAdmin):
    # a. Customize the fields displayed on the list page
    list_display = ('title', 'author', 'publication_year')

    # b. Add filters to the sidebar
    list_filter = ('author', 'publication_year')

    # c. Enable searching on specific fields
    search_fields = ('title', 'author')

# 2. Register the model using the custom class
admin.site.register(Book, BookAdmin)

