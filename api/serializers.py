from api.models import Task
from rest_framework import serializers
from django.contrib.auth.models import User 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields= "__all__"
        read_only_fields=["id","assigned_date"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

        fields=["id","username","email","password"]

        read_only_fields=["id"]

    def create(self,validated_data):   #overriding Model serializer create()
        return User.objects.create_user(**validated_data)
