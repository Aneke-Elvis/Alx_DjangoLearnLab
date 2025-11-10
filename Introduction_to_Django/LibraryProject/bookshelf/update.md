# Update Operation

>>> retrieved_book = Book.objects.get(title="1984")
>>> retrieved_book.title = "Nineteen Eighty-Four"
>>> retrieved_book.save()
# Output: (no output)
>>> print(Book.objects.get(pk=retrieved_book.pk).title)
Nineteen Eighty-Four