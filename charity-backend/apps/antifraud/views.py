from django.core.exceptions import ValidationError as DjangoValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.common.validators import validate_iin
from apps.users.permissions import IsAuthor

from .models import FraudProfile
from .serializers import FraudProfileSerializer


class FraudProfileByIINView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = FraudProfileSerializer
    lookup_field = "iin"

    def get_queryset(self):
        return FraudProfile.objects.all()

    def get(self, request, *args, **kwargs):
        iin = kwargs["iin"]
        try:
            validate_iin(iin)
        except DjangoValidationError as exc:
            return Response({"detail": exc.messages[0]}, status=status.HTTP_400_BAD_REQUEST)
        profile = get_object_or_404(self.get_queryset(), iin=iin)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
