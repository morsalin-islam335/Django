from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 30)
    roll = models.IntegerField(primary_key = True)
    address = models.TextField()
    fathers_name = models.TextField(default = 'Mostafa Ali')
    mothers_name = models.TextField(default = "Monowara Begum")
    #py manage.py makemigrations  
    #py manage.py migrate

    def __str__(self):
        return f"name{self.name} -> roll {self.roll}"



class modelTeacher(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 30)


    def __str__(self):
        return f"teacher name -> {self.name} teacher's id -> {self.id} subject -> {self.subject}"
