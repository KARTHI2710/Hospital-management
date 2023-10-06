
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='registrationsummary'),
    path('addpatient',views.add_patient,name='addpatient'),
   # path('addpatient',views.store_patientdata,name='storepatientdata')
]