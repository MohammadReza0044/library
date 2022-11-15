from django.urls import path
from .views import Book_list , search , index , member_create

urlpatterns = [
    path('', index , name= 'index'),
    path('books/', Book_list.as_view() , name= 'book_list'),
    path('member_create/' , member_create , name= 'member_create'),
    path('search/', search , name= 'search'),
]
