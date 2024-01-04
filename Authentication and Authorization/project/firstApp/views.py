from django.shortcuts import render

# Create your views here.

from . import sign_in_form

form = sign_in_form.sign_in

def home(request):
    return render(request, 'index.html', {"form": form})
