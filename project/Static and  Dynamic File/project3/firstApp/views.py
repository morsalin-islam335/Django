from django.shortcuts import render


#create data to  pass it as dictionary

from django.http import HttpResponse



def home(request):
    return render(request, "app.html")

