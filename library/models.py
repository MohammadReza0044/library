from django.db import models

class Member(models.Model):
    name = models.CharField(max_length= 100)
    family = models.CharField(max_length= 100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length= 500)

    def __str__(self):
        return self.name + ' ' + self.family

class Librarian(models.Model):
    name = models.CharField(max_length= 100)
    family = models.CharField(max_length= 100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length= 500)

    def __str__(self):
        return self.name + ' ' + self.family



class Author(models.Model):
    full_name = models.CharField(max_length= 200)
    country = models.CharField(max_length= 200)

    def __str__(self):
        return self.full_name

class Subject(models.Model):
    subject = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.subject

class Category(models.Model):
    category = models.CharField(max_length= 200)

    def __str__(self):
        return self.category


class Book(models.Model):
    name = models.CharField(max_length= 200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE,)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE,)
    category = models.ForeignKey(Category, on_delete= models.CASCADE,)
    published_date = models.DateField()

    def __str__(self):
        return self.name


class Reserved_Book(models.Model):
    memmber = models.ForeignKey(Member, on_delete= models.CASCADE,)
    book = models.ForeignKey(Book, on_delete= models.CASCADE,)
    reserve_date_start = models.DateField()
    reserve_date_end = models.DateField()

    
    def __str__(self):
        return self.memmber.name + " " + self.memmber.family