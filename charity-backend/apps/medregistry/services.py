from datetime import date

from .models import MedicalRecord


def fetch_medical_record(iin):
    return (
        MedicalRecord.objects.prefetch_related("diagnoses")
        .filter(iin=iin)
        .first()
    )


def get_primary_diagnosis_name(record):
    diagnosis = record.diagnoses.order_by("-diagnosed_date").first()
    return diagnosis.name if diagnosis else ""


def calculate_age_from_birth_date(birth_date):
    today = date.today()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )
