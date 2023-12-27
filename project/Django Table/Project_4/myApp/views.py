from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
     if request.method == "POST":
        name = request.POST.get("userName")
        email = request.POST.get("email")
        return render(request, "about.html", {"name":name, "email": email})
     elif request.method == "GET":
        name = request.GET.get("userName")
        email = request.GET.get("email")
        return render(request, "about.html", {"name":name, "email": email})

     else:
         return render(request, "about.html")

def form(request):
    # print(request.POST)
   return render(request, "form.html")


from . forms import Contact
from . forms import StudentData



def DjangoForm(request):
    # form = Contact(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data) 
    # return render(request, "django_form.html", {"form": form})

    if request.method == "POST":
        form = Contact(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["profile_pic"] # profile_pic is file name of forms.py file            
            with open("./myApp/upload/" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            print(form.cleaned_data) 
            return render(request, "django_form.html", {"form": form})
    else:
        form = Contact()
    
    return render(request, "django_form.html", {"form": form})



def  StudentFormData(request):
    if request.method == "POST":
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, "django_form.html", {"form": form})