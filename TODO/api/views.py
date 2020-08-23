from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status


from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoList(APIView):
    """List all todos or creates a new one"""
    def get(self, request):
        todos = Todo.objects.all()
        todo_data = TodoSerializer(todos, many=True)
        return Response(todo_data.data)


    def post(self, request):
        todo = TodoSerializer(data=request.data)
        if todo.is_valid():
            todo_item = todo.save()
            todo_item.completed = False
            todo_item.url = reverse('todo_one', args=[todo_item.id],request=request)
            todo_item.save()
            return Response(todo.data, status=status.HTTP_201_CREATED)
        return Response(todo.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request):
        Todo.objects.all().delete()
        return Response(None)

class TodoOne(APIView):
    """List a particular todo, updates the content
    of  a particular todo or delete the todo"""
    def get(self, request, todo_pk):
        try:
            todo = Todo.objects.get(pk=todo_pk)
            todo_data = TodoSerializer(todo)
            return Response(todo_data.data, status=200)
        except Todo.DoesNotExist:
            return Response(None, status=400)
    
    def patch(self, request, todo_pk):
        try:
            todo_item = Todo.objects.get(pk=todo_pk)
            serializer = TodoSerializer(todo_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Todo.DoesNotExist:
            return Response(None, status= 400)

    def delete(self, request, todo_pk):
        Todo.objects.get(pk=todo_pk).delete()
        return Response(None)

    
