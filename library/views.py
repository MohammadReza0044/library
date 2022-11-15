from django.shortcuts import render , redirect
from django.views import View
from django.contrib import messages
from django.db.models import Q

from .models import Book
from .forms import MemberForm

def index(request):
    return render (request, 'library/index.html')


class Book_list(View):
    
    def get (self , request):
        book = Book.objects.all()
        return render (request, 'library/book_list.html', {'book':book})


def member_create(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name'] 
        family = form.cleaned_data ['family'] 
        phone_number = form.cleaned_data ['phone_number'] 
        address = form.cleaned_data ['address'] 
        form.save()
        messages.add_message(request, messages.SUCCESS, ' با موفقیت ثبت شد')
        return redirect('/member_create/')
    else:
        form = MemberForm
        return render(request,'library/member_create.html', {'form':form})




def search (request, **kwargs):
    if request.method == 'GET':
        query = request.GET.get('search')
    book_result = Book.objects.filter(
        Q(name__icontains=query) | Q(author__full_name=query) | Q(subject__subject=query) 
    ) 
        
  
    return render (request, 'library/book_search.html' , {'book_result':book_result, 'query':query})