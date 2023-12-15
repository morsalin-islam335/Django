from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("This is navigation app home page")

myDict = {"authors":"Morsalin Islam","Age":18,
          "courses":[
              {"name":"C","price":2000},
              {'name':"C++", "price":4000},
              {"name":"Python", "price":4000},
              {"name":"Django", "price":8000}
                    ]}
def details(request):
    return render(request, "navigation/details.html",myDict)


def contact(request):
    return render(request, "navigation/contact.html")
    