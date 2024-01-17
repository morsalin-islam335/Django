from django.contrib import admin

# Register your models here.

from . models import TaskCategory

admin.site.register(TaskCategory)
