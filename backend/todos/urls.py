from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path("", views.ListTodo.as_view()),
    path("<int:pk>/", views.DetailTodo.as_view()),
]
