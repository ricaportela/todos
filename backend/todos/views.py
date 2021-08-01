from django.contrib.auth.models import Group, User
from rest_framework import generics, permissions, viewsets
from .serializers import GroupSerializer, UserSerializer
from .my_permissions import UsersGroupsPermission

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    permission_classes = (UsersGroupsPermission,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
