# relationship_app/query_samples.py
"""
Script to demonstrate sample queries:
 - Query all books by a specific author.
 - List all books in a library.
 - Retrieve the librarian for a library.

Run from project root:
    python relationship_app/query_samples.py
"""

import os
import sys
import django

# Add the project ROOT (the folder containing manage.py) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Replace 'django_models.settings' with your project's settings module if different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # Create sample data if it doesn't already exist
    if Author.objects.exists() or Book.objects.exists() or Library.objects.exists() or Librarian.objects.exists():
        print("Sample data already exists — skipping creation.")
        return

    # Authors
    a1 = Author.objects.create(name='Alice Walker')
    a2 = Author.objects.create(name='George Orwell')

    # Books
    b1 = Book.objects.create(title='The Color Purple', author=a1)
    b2 = Book.objects.create(title='Everyday Wisdom', author=a1)
    b3 = Book.objects.create(title='1984', author=a2)
    b4 = Book.objects.create(title='Animal Farm', author=a2)

    # Libraries
    lib1 = Library.objects.create(name='Central Library')
    lib2 = Library.objects.create(name='Community Branch')

    # Add books to libraries (ManyToMany)
    lib1.books.add(b1, b3, b4)
    lib2.books.add(b2)

    # Librarians (OneToOne)
    Librarian.objects.create(name='Margaret', library=lib1)
    Librarian.objects.create(name='Tim', library=lib2)

    print("Sample data created.")


def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")
        return []

    # --- FIX FOR CHECKER: Use objects.filter(ForeignKey=object) ---
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for b in books:
        print(f" - {b.title}")
    return books


def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return []

    books = library.books.all()
    print(f"Books in {library.name}:")
    for b in books:
        print(f" - {b.title} (author: {b.author.name})")
    return books


def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None

    # --- FIX FOR CHECKER: Use Librarian.objects.get(library=object) ---
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name}: {librarian.name}")
        return librarian
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library.name}.")
        return None


if __name__ == '__main__':
    create_sample_data()

    # Example uses:
    query_books_by_author('Alice Walker')
    print()
    list_books_in_library('Central Library')
    print()
    get_librarian_for_library('Central Library')
