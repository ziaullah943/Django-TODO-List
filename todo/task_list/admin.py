from django.contrib import admin

# Register your models here.
from task_list.models import Task
# from .models import  * 
admin.site.register(Task)
