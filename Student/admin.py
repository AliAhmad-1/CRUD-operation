from django.contrib import admin
from .models import Student
from parler.admin import TranslatableAdmin

@admin.register(Student)
class StudentModelAdmin(TranslatableAdmin):
    list_display=['id','name','email','city','password']
