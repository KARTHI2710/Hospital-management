
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='registrationsummary'),
    path('addpatient',views.add_patient,name='addpatient'),
   # path('addpatient',views.store_patientdata,name='storepatientdata')
    path('deletepatient/<pid>',views.delete_patient,name='deletepatient'),
    path('editpatient/<pid>',views.edit_patient,name='editpatient'),
    path('qrcode/<pid>',views.generate_qrcode,name='qrcode'),
    path('barcode/<pid>',views.generate_barcode,name='barcode'),
    path('refdr',views.refdr_page,name='refdr'),
    path('addrefdr',views.addrefdr_page,name='addrefdr'),
    path('deleterefdr/<docid>',views.delete_refdr,name='delete_refdr'),
    path('editrefdr/<docid>',views.edit_refdr,name='edit_refdr'),
    path('testmaster',views.testmaster_page,name='testmaster'),
    path('addtest',views.addtest_page,name='addtest'),
    path('deletetest/<tid>',views.delete_test,name='deletetest'),
    path('edittest/<tid>',views.edit_test,name='edittest'),
    path('pathologistmaster',views.pathologistmaster,name='pathologist')
]