from django.db import models


class TodoModel (models.Model) :
    text = models.CharField(max_length=100)
    IsDone = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class CalenderModel (models.Model) : 
    text = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    IsDone = models.BooleanField(default=False)