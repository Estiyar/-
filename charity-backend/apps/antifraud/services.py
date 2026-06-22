from .models import FraudProfile

BLOCK_THRESHOLD = 70
REVIEW_THRESHOLD = 40


def fetch_fraud_profile(iin):
    return FraudProfile.objects.filter(iin=iin).first()


def get_risk_score(iin):
    profile = fetch_fraud_profile(iin)
    if profile is None:
        return None
    return profile.risk_score


def is_blocked(iin):
    score = get_risk_score(iin)
    return score is not None and score >= BLOCK_THRESHOLD


def needs_review(iin):
    score = get_risk_score(iin)
    return score is not None and REVIEW_THRESHOLD <= score < BLOCK_THRESHOLD
