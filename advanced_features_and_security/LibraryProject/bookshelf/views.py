from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Book
from .forms import BookForm
from django.db.models import Q


# ============================================
#   LIST BOOKS – Requires View Permission
# ============================================
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# ============================================
#   CREATE BOOK – Requires Create Permission
# ============================================
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully.")
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/book_form.html', {'form': form})


# ============================================
#   EDIT BOOK – Requires Edit Permission
# ============================================
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/book_form.html', {'form': form})


# ============================================
#   DELETE BOOK – Requires Delete Permission
# ============================================
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('book_list')

    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

@login_required
def search_books(request):
    query = request.GET.get("q", "")

    results = Book.objects.none()

    if query:
        # SAFE: ORM prevents SQL injection
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )

    return render(request, "bookshelf/book_list.html", {
        "books": results,
        "query": query
    })