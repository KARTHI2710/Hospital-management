from django import forms
from .models import Report_db
from .models import User
from django.contrib.auth.forms import UserCreationForm


class ReportForm(forms.ModelForm):
    Reportcode=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','min':0}))
    ReportName=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Report_db
        fields = '__all__'


class RichForm(forms.ModelForm):
    class Meta:
        model = Report_db
        exclude = ['Reportcode', 'ReportName']


class CustomUserCreationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']