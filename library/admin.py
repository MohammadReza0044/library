from django.contrib import admin

from .models import Member , Librarian , Book , Author , Subject , Category , Reserved_Book


admin.site.register(Member)
admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Reserved_Book)