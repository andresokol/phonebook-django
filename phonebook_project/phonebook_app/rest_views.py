from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer


class PersonViewV1(APIView):
    def get(self, request, person_id: int):
        person = get_object_or_404(Person, id=person_id)
        # comment from feature-1
        serialized = PersonSerializer(person)
        # comment 2 from feature-1
        return Response(serialized.data)

    def post(self, request, person_id: int, age: int):
        person = get_object_or_404(Person, id=person_id, age=age)
        serialized = PersonSerializer(person, data=request.data)

        if serialized.is_valid():
            # comment for feature-2
            # is is required?
            serialized.save()
            # i think this is a mistake
            # serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# ----


# ----


class PersonViewV2(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    # queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        age = self.kwargs.get("age")
        return Person.objects.filter(age=age)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
