from django.shortcuts import redirect, render
from django.urls import reverse
from books.models import Book
from django.core.paginator import Paginator

book_paginator = Paginator(Book.objects.all(), 1)

def books_view(request):
    return redirect(reverse("catalog"))

def show_catalog(request):
    context = {
        'books': Book.objects.all(),
        'catalog_path': reverse('catalog'),
    }
    return render(request, 'base.html', context)

def show_book(request, date):
    book = Book.objects.filter(pub_date = date)
    current_page = book_paginator.get_page(book[0].id)
    previous_date = ''
    next_date = ''
    if current_page.has_previous():
        previous_date = book_paginator.get_page(current_page.previous_page_number()).object_list[0].pub_date
    if current_page.has_next():
        next_date = book_paginator.get_page(current_page.next_page_number()).object_list[0].pub_date

    context = {
        'books': book,
        'catalog_path': reverse('catalog'),
        'previous_date': previous_date,
        'next_date': next_date
    }
    return render(request, 'books/books_list.html', context)