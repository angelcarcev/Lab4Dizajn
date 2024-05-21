from django.shortcuts import render

from .models import Book
from .forms import BookForm


# Create your views here.

def index(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {"books": book}
    return render(request, 'index.html', context=context)

def books(request):
    b = Book.objects.all()
    context = {"books": b}
    return render(request, 'books.html', context=context)

def addbook(request):
    if request.method == "POST":
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
    else:
        book = BookForm()

    return render(request, "add_book.html", {"form": book})
