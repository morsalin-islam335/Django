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


def DjangoForm(request):
    form = Contact(request.POST)
    if form.is_valid():
        print(form.cleaned_data) 
    return render(request, "django_form.html", {"form": form})

