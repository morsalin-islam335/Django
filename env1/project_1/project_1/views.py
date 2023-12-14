
from django.http import HttpResponse

def aboutMe(request):
    return HttpResponse("hello my name is Morsalin Islam")

def homePage(resonse):
    return HttpResponse("This is home page")
    
