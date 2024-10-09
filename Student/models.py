from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Student(TranslatableModel):
    translations=TranslatedFields(
        name=models.CharField(max_length=50,blank=False,null=False),
        email=models.EmailField(blank=False,null=False),
        city=models.CharField(max_length=50,null=False,blank=False)
    )

    password=models.CharField(max_length=50)

    def __str__(self):
        return self.password
    def save(self, *args, **kwargs):
        self.password=make_password(self.password)
        super(Student,self).save(*args, **kwargs)

