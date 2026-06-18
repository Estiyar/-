from datetime import date

from apps.antifraud.models import FraudProfile, RiskLevel
from apps.medregistry.models import Gender, MedicalDiagnosis, MedicalRecord

AUTHOR_IIN = "880420301999"
OTHER_AUTHOR_IIN = "930615402345"
RECIPIENT_IIN = "850315301234"
ALT_RECIPIENT_IIN = "920712401567"
THIRD_RECIPIENT_IIN = "780901300789"
HIGH_RISK_IIN = "990101300999"


def _seed_fraud_profile(iin, full_name, risk_score, risk_level, reasons):
    FraudProfile.objects.get_or_create(
        iin=iin,
        defaults={
            "full_name": full_name,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "reasons": reasons,
        },
    )


def _seed_recipient(iin, full_name, city, clinic, gender, diagnosis_name):
    _seed_fraud_profile(
        iin,
        full_name,
        12,
        RiskLevel.LOW,
        ["Проверенный получатель помощи"],
    )
    record, _ = MedicalRecord.objects.get_or_create(
        iin=iin,
        defaults={
            "full_name": full_name,
            "birth_date": date(1990, 1, 1),
            "gender": gender,
            "city": city,
            "clinic": clinic,
        },
    )
    if diagnosis_name and not record.diagnoses.exists():
        MedicalDiagnosis.objects.create(
            record=record,
            name=diagnosis_name,
            stage="I",
            diagnosed_date=date(2024, 1, 1),
        )


def seed_fundraiser_iin_fixtures():
    _seed_fraud_profile(
        AUTHOR_IIN,
        "Асель Бекенова",
        5,
        RiskLevel.LOW,
        ["Нет подозрительной активности"],
    )
    _seed_fraud_profile(
        OTHER_AUTHOR_IIN,
        "Нурлан Сейтжанов",
        8,
        RiskLevel.LOW,
        ["Чистая кредитная история"],
    )
    _seed_fraud_profile(
        HIGH_RISK_IIN,
        "Ерболат Мукашев",
        92,
        RiskLevel.HIGH,
        ["Множественные мошеннические заявки"],
    )
    _seed_recipient(
        RECIPIENT_IIN,
        "Айгуль Смагулова",
        "Алматы",
        "Городская поликлиника №5",
        Gender.FEMALE,
        "Онкология",
    )
    _seed_recipient(
        ALT_RECIPIENT_IIN,
        "Данияр Касымов",
        "Астана",
        "Республиканский госпиталь",
        Gender.MALE,
        "Сахарный диабет",
    )
    _seed_recipient(
        THIRD_RECIPIENT_IIN,
        "Гульнара Толеуова",
        "Шымкент",
        "Областная больница",
        Gender.FEMALE,
        "Порок сердца",
    )
