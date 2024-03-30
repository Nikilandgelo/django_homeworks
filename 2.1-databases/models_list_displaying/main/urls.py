from django.urls import register_converter
from books.converters import DateConverter
from django.urls import path
from books.views import books_view, show_book, show_catalog

register_converter(DateConverter, "date")

urlpatterns = [
    path('', books_view),
    path('books/', show_catalog, name='catalog'),
    path('books/<date:date>', show_book),
]