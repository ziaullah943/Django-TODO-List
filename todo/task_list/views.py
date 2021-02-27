from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from task_list.models import Task
from task_list.forms import TaskForm

def index(request):
    tasks=Task.objects.all()
    form=TaskForm()

    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks,'form':form}
    return render(request,'task_list/list.html',context)
def updateTask(request,pk):
    task=Task.objects.get(id=pk) 
    form=TaskForm(instance=task)

    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'task_list/update_task.html',context)


def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={'item':item}

    return render(request,'task_list/delete.html',context)







