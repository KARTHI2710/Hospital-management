from django.shortcuts import render,redirect
from django.db import connection
from .models import Refdr_db,Test_db,Patient_db,Pathologist_db
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
        patient.delete()
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
    obj=Refdr_db.objects.all()
    print(obj)
    return render(request,"refdr.html",{'keys':obj})

def addrefdr_page(request):
    latest_did=generate_did()
    next_did=generate_next_did(latest_did)

    if request.method=="POST":
        docid=next_did
        docname=request.POST['docname']
        specalization=request.POST['spec']
        qual=request.POST['qualification']
        address=request.POST['address']
        mobile=request.POST['mobile']
        
        docobj=Refdr_db(docid,docname,specalization,address,qual,mobile) 
        docobj.save() 
        return redirect('/refdr')
    return render(request,'addrefdr.html',{'key':next_did})


def generate_did():
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT MAX(Doctorcode) FROM hospitalapp_refdr_db")
        latest_test_number = cursor.fetchone()[0]
        return latest_test_number
    except Exception as e:
        print("Error fetching latest doctor number:", str(e))
        return None

def generate_next_did(did):
    if did==None:
        return 'D00001'
    else:
        prefix='D'
        numeric_part=did[1:]
        next_id=int(numeric_part)+1
        next_doctor_number = f"{prefix}{next_id:05}"  # Format as "D00001"
        return next_doctor_number 
    
def delete_refdr(request,docid):
    obj=Refdr_db.objects.get(pk=docid)
    obj.delete()
    return redirect('/refdr')

def edit_refdr(request,docid):
    obj=Refdr_db.objects.get(pk=docid)
    if request.method=='POST':
        obj.Doctorcode=request.POST['d_id']
        obj.DoctorName=request.POST['docname']
        obj.Specialization=request.POST['spec']
        obj.Address=request.POST['address']
        obj.Qualification=request.POST['qualification']
        obj.Mobile=request.POST['mobile']
        obj.save()
        return redirect('/refdr')
    return render(request,'editrefdr.html',{'key':obj})


def testmaster_page(request):
    obj=Test_db.objects.all()
    return render(request,'testmaster.html',{'keys':obj})


def addtest_page(request):
    latest_test_id=generate_testid()
    next_test_id=generate_next_testid(latest_test_id)
    if request.method=='POST':
        testid=next_test_id
        testname=request.POST['tname']
        specimen=request.POST['spec']
        obj=Test_db(testid,testname,specimen)
        obj.save()
        return redirect('/testmaster')
    return render(request,'addtest.html',{'key':next_test_id})


def generate_testid():
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT MAX(Testcode) FROM hospitalapp_test_db")
        latest_test_number = cursor.fetchone()[0]
        return latest_test_number
    except Exception as e:
        print("Error fetching latest test number:", str(e))
        return None

def generate_next_testid(testid):
    if testid==None:
        return 'T00001'
    else:
        prefix='T'
        numeric_part=testid[1:]
        next_id=int(numeric_part)+1
        next_test_number = f"{prefix}{next_id:05}"  # Format as "T00001"
        return next_test_number 
    
def delete_test(request,tid):
    obj=Test_db.objects.get(pk=tid)
    obj.delete()
    return redirect('/testmaster')

def edit_test(request,tid):
    obj=Test_db.objects.get(pk=tid)
    if request.method=='POST':
        obj.Testcode=request.POST['tid']
        obj.TestName=request.POST['tname']
        obj.speicmentype=request.POST['spec']
        obj.save()
        return redirect('/testmaster')
    return render(request,'edittest.html',{'key':obj})


def pathologistmaster(request):
    obj=Pathologist_db.objects.all()
    return render(request,'pathologistmaster.html',{'keys':obj})