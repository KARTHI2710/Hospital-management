from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Patient_db(models.Model):
    uhid=models.CharField(max_length=10,primary_key=True)
    title=models.CharField(max_length=10)
    patientname=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    dob=models.CharField(max_length=10)
    age=models.IntegerField()
    email=models.EmailField()
    mobile=models.IntegerField()
    refdr=models.CharField(max_length=20)
    selected_test=models.CharField(max_length=50)

    def __str__(self):
        return self.uhid
    
class Refdr_db(models.Model):
    Doctorcode=models.CharField(max_length=10,primary_key=True)
    DoctorName=models.CharField(max_length=20)
    Specialization=models.CharField(max_length=20)
    Address=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=10)
    Mobile=models.IntegerField()

    def __str__(self):
        return self.Doctorcode

class Test_db(models.Model):
    Testcode=models.CharField(max_length=10,primary_key=True)
    TestName=models.CharField(max_length=20)
    speicmentype=models.CharField(max_length=20)

    def __str__(self):
        return self.Testcode
    
class Report_db(models.Model):
    Reportcode=models.IntegerField()
    ReportName=models.CharField(max_length=20)
    Template = RichTextField()

    def __str__(self):
        return self.ReportName
    

class Pathologist_db(models.Model):
    Doctorcode=models.CharField(max_length=10,primary_key=True)
    DoctorName=models.CharField(max_length=20)
    Specialization=models.CharField(max_length=20)
    Address=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=10)
    Mobile=models.IntegerField()
    Signature=models.ImageField(upload_to='signature/',blank=True)

    def __str__(self):
        return self.Doctorcode


class Patientreports_db(models.Model):
    
    

    

    