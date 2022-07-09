from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "", include("phonebook_app.urls", namespace="phonebook_app_namespace")
    ),
    path("todo/", include("todo.urls", namespace="todo")),
    path("admin/", admin.site.urls),
]
