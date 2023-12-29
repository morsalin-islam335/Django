from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Teacher

from . import models
def home(request):
    form_data =  models.Student.objects.all()
    return render(request, "home.html", {"data": form_data})


def deleteStudent(request, roll):
    models.Student.objects.get(pk = roll).delete()
    # return HttpResponse("delete button clicked")
    # form_data =  models.Student.objects.all()
    # return render(request, "home.html", {"data": form_data})
    return redirect("homepage")



def teacherField(request):  # that is just for model form
    if(request.method == "POST"):
        form = Teacher(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request, "modelForm.html", {"form": form})
    else:
        form = Teacher
        return render(request, "modelForm.html", {"form": form})


    
    # return render(request, "modelForm.html", {"data":[10,20,30,40]})