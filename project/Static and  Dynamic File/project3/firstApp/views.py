from django.shortcuts import render


#create data to  pass it as dictionary




def home(request):
    return render(request, "app.html")
