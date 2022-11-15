from django.urls import path
from .views import Book_list , search , index

urlpatterns = [
    path('', index , name= 'index'),
    path('books/', Book_list.as_view() , name= 'book_list'),
    path('search/', search , name= 'search'),
]
