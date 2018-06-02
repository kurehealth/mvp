from django.urls import path
from .views import CreatePatientForm,PatientsList,createPDFReport


urlpatterns = [
path('createpatient/',CreatePatientForm.as_view(success_url="/"),name='createpatient'),
path('createpdf/',createPDFReport.as_view(),name='createPDF'),
path('',PatientsList.as_view(),name='index'),
]