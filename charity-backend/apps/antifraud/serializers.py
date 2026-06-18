from rest_framework import serializers

from .models import FraudProfile


class FraudProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudProfile
        fields = ("iin", "full_name", "risk_score", "risk_level", "reasons")
