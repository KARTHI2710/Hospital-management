from django.shortcuts import render,redirect
from django.db import connection
from .models import Refdr_db,Test_db,Patient_db
import qrcode
from django.contrib import messages
from barcode import Code128
from barcode.writer import ImageWriter

# Create your views here.
def home(request):
        patient_values=Patient_db.objects.all()
        return render(request,'registrationsummary.html',{'key':patient_values})



def add_patient(request):
    latest_pid=generate_pid()
    next_pid=generate_next_pid(latest_pid)
    
    refdr_name_values=Refdr_db.objects.all()
    test_name_values=Test_db.objects.all()
    
  
    
    if request.method=='POST':
        pid=next_pid
        pname=request.POST['pname']
        title=request.POST['title']
        gender=request.POST['gender']
        age=request.POST['age']
        dob=request.POST['dob']
        email=request.POST['email']
        mobile=request.POST['mobile']
        refdr=request.POST['refdr']
        selectedtest=request.POST['test']

        obj=Patient_db(pid,title,pname,gender,dob,age,email,mobile,refdr,selectedtest)
        obj.save()

        # patient_values=Patient_db.objects.all()
        # return render(request,'registrationsummary.html',{'key':patient_values})
        return redirect('/')

    return render(request,'addpatient.html',{'pid':next_pid,'refdr_names_keys':refdr_name_values,'test_name_keys':test_name_values})



def generate_pid():
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT MAX(uhid) FROM hospitalapp_patient_db")
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
    


def delete_patient(request, pid):
    # Assuming 'Patient_db' is your model and 'pk' is the primary key field
    try:
        patient = Patient_db.objects.get(pk=pid)
        print(patient)
        print(type(patient))
       # patient.delete()
    except Patient_db.DoesNotExist:
        # Handle the case where the patient with the provided pid does not exist
        pass
    
    return redirect('/')

def edit_patient(request,pid):
    if request.method=='POST':
        p_id=pid
        pname=request.POST['pname']
        title=request.POST['title']
        gender=request.POST['gender']
        age=request.POST['age']
        dob=request.POST['dob']
        email=request.POST['email']
        mobile=request.POST['mobile']
        refdr=request.POST['refdr']
        selectedtest=request.POST['test']
        obj=Patient_db.objects.get(pk=pid)

        obj.uhid=p_id
        obj.patientname=pname
        obj.title=title
        obj.gender=gender
        obj.age=age
        obj.dob=dob
        obj.email=email
        obj.mobile=mobile
        obj.refdr=refdr
        obj.selected_test=selectedtest

        obj.save()


        # patient_values=Patient_db.objects.all()
        # return render(request,'registrationsummary.html',{'key':patient_values})
        return redirect('/')
    try:
        patient = Patient_db.objects.get(pk=pid)
        refdr_name_values=Refdr_db.objects.all()
        test_name_values=Test_db.objects.all()
        return render(request,'editpatient.html',{'key':patient,'refdr_names_keys':refdr_name_values,'test_name_keys':test_name_values})
    except Patient_db.DoesNotExist:
        # Handle the case where the patient with the provided pid does not exist
        pass

def generate_qrcode(request,pid):
    print(pid)
    # Data to be encoded
    patient=Patient_db.objects.get(pk=pid)
    data = f'''Patient Uhid : {patient.uhid}\n
Patient Name :{patient.title} {patient.patientname}\n
Gender : {patient.gender}\n
Age : {patient.age}\n
Mobile : {patient.mobile}\n
DOB : {patient.dob}\n
Selected Test : {patient.selected_test}\n
RefDr : {patient.refdr}\n
'''
    
    # Encoding data using make() function
    img = qrcode.make(data)
    
    # Saving as an image file
    img.save(f'qrcode_{patient.uhid}.png')
    # messages.success(request,"Qrcode generated successfully ! ")
    # messages.warning(request,"Qrcode generated successfully ! ")
    return redirect('/')

def generate_barcode(request,pid):
    my_code = Code128(pid, writer=ImageWriter()) 
    my_code.save(f'barcode_{pid}')
    return redirect('/')

def refdr_page(request):
    return render(request,"refdr.html")