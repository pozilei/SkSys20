from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from todos_app.models import Author, Todo
from .forms import TodoForm

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


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.description = form.cleaned_data['description']
            post.due = form.cleaned_data['due']
            post.accomplished = form.cleaned_data['accomplished']
            post.save()
            return HttpResponseRedirect('/todos_app/')
    else:
        form = TodoForm()
    return render(request, 'todos_app/create_todo.html', {'form': form})


def edit_todo(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.description = form.cleaned_data['description']
            post.due = form.cleaned_data['due']
            post.accomplished = form.cleaned_data['accomplished']
            post.save()
            return HttpResponseRedirect('/todos_app/')
    else:
        form = TodoForm(instance=post)
    return render(request, 'todos_app/edit_todo.html', {'form': form})

