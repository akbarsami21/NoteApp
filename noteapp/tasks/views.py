from django.shortcuts import get_object_or_404, render,redirect
from .models import Task

# Create your views here.
def index(request):
    tasks=Task.objects.all().order_by('-id')
    return render(request,'index.html',{'tasks':tasks})

def completed(request):
    completed_task=Task.objects.filter(completed=True)
    return render(request,'completed.html',{'ctask':completed_task})

def remaining(request):
    remaining_task=Task.objects.filter(completed=False)
    return render(request,'remaining.html',{'rtask':remaining_task})

def add_task(request):
    if request.method=='POST':
        title=request.POST['tname']
        description=request.POST['tdesc']
        due_date=request.POST['date']
        due_time=request.POST['time']
        completed = 'check' in request.POST
        
        if title!='' and description!='' and due_date!='' and due_time!='':
            todo=Task(title=title,description=description,due_date=due_date,due_time=due_time,completed=completed)
            todo.save()
            return redirect('index')
    else:
        return render(request,'add_task.html')
    return render(request,'add_task.html')

def task_detail(request,id):
    details=Task.objects.get(id=id)
    return render(request,'task_detail.html',{'task':details,'goback':False})

def toggle_complete(request,id):
    task=Task.objects.get(id=id)
    if task:
        #task.completed=not task.completed
        task.save()
        return redirect('index')


def delete(request,id):
    tasks=Task.objects.get(id=id)
    return render(request,'delete.html',{'task':tasks})

def remove(request,id):
    task=Task.objects.get(id=id)
    if task:
        task.completed=not task.completed
        task.delete()
        return redirect('index')

def update(request,id):
    tasks = get_object_or_404(Task, id=id)
    if request.method=='POST':
        title=request.POST['tname']
        description=request.POST['tdesc']
        due_date=request.POST['date']
        due_time=request.POST['time']
        completed = 'check' in request.POST


        if title and description and due_date and due_time:
            tasks.title=title
            tasks.description=description
            tasks.due_date=due_date
            tasks.due_time=due_time
            tasks.completed=completed
            tasks.save()
            return redirect('index')
        else:
            return render(request,'update.html',{'task':tasks})

    return render(request,'update.html',{'task':tasks})
