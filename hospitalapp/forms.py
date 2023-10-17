from django import forms
from .models import Report_db


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