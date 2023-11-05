from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # If you want to associate tasks with users


# Developers create API on the server and allow the client/frontend to talk to it.

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField(null=True,blank=True)
    # due_date = models.DateTimeField(null=True,blank=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    # photos = models.ManyToManyField(TaskPhoto, blank=True)  # Assuming you have a Photo model
    is_complete = models.BooleanField(default=False,blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # If you want to associate tasks with users
    image=models.FileField(blank=True,null=True,max_length=255)
    def __str__(self):
        return self.title

""" class TaskPhoto(models.Model):
    image = models.ImageField(upload_to='task_photos/')
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return "%s" % (self.task.title

    def __str__(self):
        return str(self.task.title) """



""" from django.db import models
from django.contrib.auth.models import User
from Photos.models import *

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateTimeField()
    priority=models.CharField(max_length=10, choices=(('Low','Low'),('Medium','Medium'),('High','High')))
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    photos=models.ManyToManyField(Photo, blank=True)
    
    def __str__(self):
        return self.title



     """
