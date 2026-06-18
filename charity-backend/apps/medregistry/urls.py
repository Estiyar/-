from django.urls import path

from .views import MedicalRecordByIINView

urlpatterns = [
    path("<str:iin>/", MedicalRecordByIINView.as_view(), name="medregistry-by-iin"),
]
