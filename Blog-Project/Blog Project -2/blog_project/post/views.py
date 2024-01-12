from django.shortcuts import render, redirect

# Create your views here.
from . models import Post

from . postForm import PostForm
def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            print("add post successfully")
            return redirect('homepage')
    form = PostForm()
    return render(request, 'post.html',{"form":form})
       
from . import models


def editPost(request, id): 
    edited_post = Post.objects.get(pk = id) # we receive here previous edited post 
    

    if(request.method == "POST"):#post request

        form = PostForm(request.POST,instance= edited_post)

        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = PostForm(instance = edited_post)
        return render(request, 'post.html', {"form": form})        
    


def deletePost(request, id):
    data =Post.objects.get(pk = id)
    data.delete() # delete from database
    return redirect("homepage")



