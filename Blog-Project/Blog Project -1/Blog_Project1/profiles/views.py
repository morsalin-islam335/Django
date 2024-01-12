from django.shortcuts import render, redirect

# Create your views here.
from . import forms
def addProfile(request):
    if request.method == "POST":
        profile = forms.ProfileForm(request.POST) 
        if profile.is_valid():
            profile.save()
            print("add profile successfully")
            return redirect("add_profile")
    form = forms.ProfileForm()
    return render(request, "profile.html", {"form": form})

