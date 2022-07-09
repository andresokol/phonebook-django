from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import TodoTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = "__all__"


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TodoTask.objects.all()


def todo_list_v1(request):
    return render(
        request,
        "todo/todo_v1.html",
        {"tasks": TodoTask.objects.all()},
    )


def todo_list_v2(request):
    return render(request, "todo/todo_v2.html")
