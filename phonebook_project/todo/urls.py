from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import TaskViewSet, todo_list_v1, todo_list_v2

app_name = "todo"

router = SimpleRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("v1/", todo_list_v1),
    path("v2/", todo_list_v2),
    path("", include(router.urls)),
]
