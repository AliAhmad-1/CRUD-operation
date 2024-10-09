from Student.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=100,write_only=True,style={'input_type':'password'})
    name=serializers.CharField(max_length=100,required=True)
    city=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    def create(self,validated_data):
        return Student.objects.create(**validated_data)