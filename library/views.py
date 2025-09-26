from django.shortcuts import render
from .models import Book

# Create your views here.
def library(request):
    beginner_books = Book.objects.filter(level='beginner')
    intermediate_books = Book.objects.filter(level='intermediate')
    advanced_books = Book.objects.filter(level='advanced')

    return render(request, 'pages/library.html', {
        'beginner_books': beginner_books,
        'intermediate_books': intermediate_books,
        'advanced_books': advanced_books,
    })




