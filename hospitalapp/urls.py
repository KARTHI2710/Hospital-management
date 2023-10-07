
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
    path('refdr',views.refdr_page,name='refdr')
]