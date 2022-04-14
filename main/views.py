from django.shortcuts import render
from .models import Task


# Create your views here.

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'main/todo_list.html', {'tasks': tasks})


def completed_todo_list(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'main/completed_todo_list.html', {'todo': task})
