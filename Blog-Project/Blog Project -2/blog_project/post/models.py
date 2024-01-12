from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
