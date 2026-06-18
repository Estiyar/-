from django.core.exceptions import ValidationError as DjangoValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.common.validators import validate_iin
from apps.users.permissions import IsAuthor

from .models import MedicalRecord
from .serializers import MedicalRecordSerializer


class MedicalRecordByIINView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = MedicalRecordSerializer
    lookup_field = "iin"

    def get_queryset(self):
        return MedicalRecord.objects.prefetch_related("diagnoses")

    def get(self, request, *args, **kwargs):
        iin = kwargs["iin"]
        try:
            validate_iin(iin)
        except DjangoValidationError as exc:
            return Response({"detail": exc.messages[0]}, status=status.HTTP_400_BAD_REQUEST)
        record = get_object_or_404(self.get_queryset(), iin=iin)
        serializer = self.get_serializer(record)
        return Response(serializer.data)
