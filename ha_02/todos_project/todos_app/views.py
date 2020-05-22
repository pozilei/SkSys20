from django.shortcuts import render
from todos_app.models import Author, Todo
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todos_app/index.html', context=context)


def impressum(request):
    author_list = Author.objects.all()
    context = {
        'author_list': author_list,
    }
    return render(request, 'todos_app/impressum.html', context=context)


def remove(request, pk):
    elm = Todo.objects.get(pk=pk)
    elm.delete()
    return HttpResponseRedirect('/todos_app/')