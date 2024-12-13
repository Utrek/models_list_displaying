from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from.models import Book

def index(request):
    return redirect('books/')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books':books}
    return render(request, template, context)

def show_book(request, pub_date):
    template = 'books/book.html'
    book = Book.objects.get(pub_date=pub_date)
    books = Book.objects.all().order_by('pub_date')
    next_book = books.filter(pub_date__gt=book.pub_date).first()
    context = {'book': book}
    if next_book:
        context['next_book'] = next_book
        context['has_next_book'] = True
    previous_book = books.filter(pub_date__lt=book.pub_date).last()
    if previous_book:
        context['previous_book'] = previous_book
        context['has_previous_book'] = True
    return render(request, template, context)






    


    
   