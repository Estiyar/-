from .models import FraudProfile, RiskLevel


def fetch_fraud_profile(iin):
    return FraudProfile.objects.filter(iin=iin).first()


def is_high_risk(iin):
    profile = fetch_fraud_profile(iin)
    if profile is None:
        return False
    return profile.risk_level == RiskLevel.HIGH
