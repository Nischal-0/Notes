from django.shortcuts import render, HttpResponse, redirect
from .models import Note

# Create your views here.

def index(request):
    tasks= Note.objects.all()
    
    total_task=tasks.count()
    
    context={
        'tasks':tasks,
        'total_task':total_task
    }
    
    return render(request,'index.html',context)
    
def create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')

        if title and description:
            Note.objects.create(title=title,description=description)
            return redirect('index')
        else:
            context={
                'error': 'Both fields required'
            }
            return render(request,'create.html',context)

    
    return render(request,'create.html')


def edit(request,id):
    
    task=Note.objects.get(id=id)

    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        
        task.title = title
        task.description = description
        task.save()
        
        return redirect('index')
        
    context={
        'task':task
    }
    
    return render (request,'edit.html',context)


def delete(request,id):
    if request.method == "POST":
        task=Note.objects.get(id=id)
        task.delete()
        return redirect ('index')
    
    
 