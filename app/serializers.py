from rest_framework import serializers
from .models import TodoModel, CalenderModel




class TodoSeriailzer (serializers.ModelSerializer) : 
    class Meta : 
        model = TodoModel
        fields = '__all__'
    

class CalendeerSerialzier (serializers.ModelSerializer) : 
    class Meta :
        model = CalenderModel
        fields = '__all__'