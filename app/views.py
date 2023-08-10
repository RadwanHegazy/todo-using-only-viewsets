from rest_framework import generics, viewsets, filters
from .models import TodoModel, CalenderModel
from .serializers import TodoSeriailzer, CalendeerSerialzier


class TodoView (viewsets.ModelViewSet) :
    queryset = TodoModel.objects.all()
    serializer_class = TodoSeriailzer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class CalnderView (viewsets.ModelViewSet) :
    queryset = CalenderModel.objects.all()
    serializer_class = CalendeerSerialzier
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']