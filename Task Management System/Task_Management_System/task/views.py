from django.shortcuts import render, redirect

# Create your views here.
from . models import Task
def home(request):
    tasks = Task.objects.all()
    
    # for task in tasks:
    #     for category in task.category:
    #         print("category: ", category.category_name)


    return render(request, 'home.html', {'tasks': tasks})


from . forms import TaskForm


def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = TaskForm()
    return render(request, 'addTask.html',{"form":form})


from . models import Task

def editTask(request, id):
    task = Task.objects.get(id = id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = TaskForm(instance=task)
    return render(request, 'editTask.html', {"form":form})





def deleteTask(request, id):
    task  = Task.objects.get(id = id)
    task.delete()
    
    return redirect("homepage")

