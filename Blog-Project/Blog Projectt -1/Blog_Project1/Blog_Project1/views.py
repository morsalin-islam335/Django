from django.shortcuts import render
from post.models import Post



def homepage(request):
    data = Post.objects.filter()
    return render(request, "homepage.html", {"postData":data})


