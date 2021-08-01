from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path("", views.ListTodo.as_view()),
    path("<int:pk>/", views.DetailTodo.as_view()),
]
