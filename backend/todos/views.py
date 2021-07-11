from rest_framework import generics
from rest_framework import permissions

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
