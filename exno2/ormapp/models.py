from django.db import models
from django.contrib import admin

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    dateofpublication = models.DateField()
    genre = models.CharField(max_length=30)
    code = models.CharField(max_length=20, primary_key=True)

class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "price", "dateofpublication", "genre", "code")
