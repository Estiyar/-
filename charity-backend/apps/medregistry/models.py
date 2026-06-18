from django.db import models


class Gender(models.TextChoices):
    MALE = "male", "Мужской"
    FEMALE = "female", "Женский"


class MedicalRecord(models.Model):
    iin = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=8, choices=Gender.choices)
    city = models.CharField(max_length=128)
    clinic = models.CharField(max_length=255)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.iin})"


class MedicalDiagnosis(models.Model):
    record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name="diagnoses",
    )
    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=64, blank=True)
    diagnosed_date = models.DateField()

    class Meta:
        ordering = ["-diagnosed_date"]

    def __str__(self):
        return f"{self.name} — {self.record.full_name}"
