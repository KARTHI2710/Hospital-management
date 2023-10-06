from django.shortcuts import render,redirect
from django.db import connection
from .models import Refdr_db

# Create your views here.
def home(request):
    return render(request,'registrationsummary.html')

def add_patient(request):
    latest_pid=generate_pid()
    next_pid=generate_next_pid(latest_pid)
    print(next_pid)

    refdr_name_values=Refdr_db.objects.all()
    
    print(refdr_name_values)
    
    if request.method=='POST':
        pid=next_pid
        #pname=request.POST['pname']

        return redirect('/')

    return render(request,'addpatient.html',{'refdr_names_keys':refdr_name_values})

def store_patientdata(request):

    if request.method=='POST':
        pass


def generate_pid():
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT MAX(uhid) FROM Patient_db")
        latest_test_number = cursor.fetchone()[0]
        return latest_test_number
    except Exception as e:
        print("Error fetching latest patient number:", str(e))
        return None

def generate_next_pid(pid):
    if pid==None:
        return 'P00001'
    else:
        prefix='P'
        numeric_part=pid[1:]
        next_id=int(numeric_part)+1
        next_patient_number = f"{prefix}{next_id:05}"  # Format as "P00001"
        return next_patient_number 
    
def populate_refdr():
    cursor=connection.cursor()
    cursor.execute("select DoctorName from ")