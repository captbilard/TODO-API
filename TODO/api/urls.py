from django.urls import path, include
# from rest_framework import routers

from . import views

# router = routers.SimpleRouter()

# router.register('todos', TodoListView)

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<int:todo_pk>/', views.TodoOne.as_view(), name='todo_one'),
]
