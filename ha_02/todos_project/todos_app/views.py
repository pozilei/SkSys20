from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import TodoForm

# Create your views here.

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