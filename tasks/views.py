from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from tasks.models import Task
from tasks.forms import TaskForm

def task_create(request):
    if request.method == 'POST':
        #将用户提交的书与TaskForm表单绑定
        form = TaskForm(request.POST)
        #表单验证，如果表单有效，将数据存入数据库
        if form.is_valid():
            form.save()
            #跳转到任务清单
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {"form": form,})

def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    return redirect(reverse('tasks:task_list'))

def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
    else:
        form = TaskForm(instance=task_obj)
    return render(request, 'tasks/task_form.html', {"form" : form, "object":task_obj})

def task_detail(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {"task": task_obj, })

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

