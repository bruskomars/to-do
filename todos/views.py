from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST.get('task')

    Task.objects.create(
        task=task,
    )

    return redirect('home')

def markDone(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.save()

    return redirect('home')

def markUndone(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = False
    task.save()

    return redirect('home')

def editTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        edit_task = request.POST.get('task')

        task.task = edit_task
        task.save()

        return redirect('home')

    context = {
        'task':task
    }
    return render(request, 'edit.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return redirect('home')