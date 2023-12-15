from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # return HttpResponse("this is a home page of this page")
    return render(request, "index.html")
