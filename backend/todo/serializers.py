from rest_framework import serializers

from .models import Todo, Mission

from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
        

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']



# Serializers define the API representation.
class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['Ref_Rem', 'Ref_Track', 'date_dep', 'date_dest', 'status']