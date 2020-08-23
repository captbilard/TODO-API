from django.shortcuts import render
from rest_framework import viewsets


from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoListView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer