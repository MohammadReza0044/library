from django.shortcuts import render, redirect
from django.views import View

from .models import Book

def index(request):
    return render (request, 'library/index.html')


class Book_list(View):
    
    def get (self , request):
        book = Book.objects.all()
        return render (request, 'library/book_list.html', {'book':book})




def search (request):
    if request.method == 'GET':
        query = request.GET.get('search')
    book_result = Book.objects.filter(name__icontains = query)
    
    
    return render (request, 'library/book_search.html' , {'book_result':book_result, 'query':query})