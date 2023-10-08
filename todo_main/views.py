from django.shortcuts import render, redirect
from todos.models import Task

def home(request):
    uncompleted_tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'uncompleted_tasks': uncompleted_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'home-todo.html', context)
