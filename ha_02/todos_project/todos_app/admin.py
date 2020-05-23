from django.contrib import admin

# Register your models here.

from todos_app.models import Author, Todo

admin.site.register(Author)
admin.site.register(Todo)

