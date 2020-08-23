from django.urls import path, include
from rest_framework import routers

from .views import TodoListView

router = routers.SimpleRouter()

router.register('todos', TodoListView)

urlpatterns = [
    path('', include(router.urls))
]
