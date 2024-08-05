from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Task
from django.views.generic import ListView, CreateView, DetailView
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completed']
    template_name = 'task_form.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
