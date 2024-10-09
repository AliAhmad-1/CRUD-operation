from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from Student.models import Student
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
class StudentViewSet(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()

    
@api_view(['GET','POST','PUT','DELETE','PATCHE'])
def student_api(request,student_id=None):
    if request.method=='GET':
        if student_id:
            stu=get_object_or_404(Student,id=student_id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
