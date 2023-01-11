from django.shortcuts import render


from rest_framework import viewsets

from .serializers import TodoSerializer, UserSerializer, MissionSerializer

from .models import Todo, Mission


from django.contrib.auth.models import User

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()