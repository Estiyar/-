from django.urls import path

from .views import FraudProfileByIINView

urlpatterns = [
    path("<str:iin>/", FraudProfileByIINView.as_view(), name="antifraud-by-iin"),
]
