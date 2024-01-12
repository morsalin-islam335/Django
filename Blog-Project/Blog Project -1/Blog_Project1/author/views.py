from django.shortcuts import render, redirect

# Create your views here.
from author import authorForm
from django.http import HttpResponse

# def addAuthor(request):
#     if(request.method == "POST"):
#         form = ProfileForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect("add_author")
#     form = ProfileForm()
#     return render(request, "author.html",{"form": form})            




def addAuthor(request):
    if request.method == 'POST':
        author_form = authorForm.ProfileForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('homepage')
        
    author_form = authorForm.ProfileForm()
    return render(request, 'author.html', {'form' : author_form})