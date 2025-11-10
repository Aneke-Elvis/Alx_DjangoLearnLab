# Delete Operation

>>> retrieved_book.delete()
(1, {'bookshelf.Book': 1})
>>> print(Book.objects.all())
<QuerySet []>