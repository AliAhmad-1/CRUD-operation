from django import forms
from .models import Student
from django.core import validators
from django.utils.translation import gettext_lazy as _
from parler.forms import TranslatableModelForm

class StudentModelForm(TranslatableModelForm):
    
    password2=forms.CharField(min_length=5,max_length=15,label=_('password(agin)'),widget=forms.PasswordInput(render_value=True,attrs={'class':"form-control"}))
    def clean_password2(self):
        pass1 = self.cleaned_data["password"]
        pass2 = self.cleaned_data["password2"]
        if pass1 != pass2:
            raise forms.ValidationError('password1 and password2 not equal..! ')

    class Meta:
        model=Student
        fields=['name','email','city','password','password2']
        help_text={'name':'here your name'}
        widgets={'name':forms.TextInput(attrs={'class':"form-control ",'placeholder':'Enter your name ..','id':'name'}),
        'city':forms.TextInput(attrs={'class':"form-control ",'placeholder':'Enter your city ..','id':'city'}),
                'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email..','id':'email'}),
                'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control','id':'password'}),

        }
        labels={'name':_('username:'),'email':_('e-mail'),'city':_('city'),'password':_('password')}
        
        help_texts={'name':''}
 



    