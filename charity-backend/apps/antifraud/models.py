from django.db import models


class RiskLevel(models.TextChoices):
    LOW = "low", "Низкий"
    MEDIUM = "medium", "Средний"
    HIGH = "high", "Высокий"


class FraudProfile(models.Model):
    iin = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=255)
    risk_score = models.PositiveSmallIntegerField()
    risk_level = models.CharField(max_length=8, choices=RiskLevel.choices)
    reasons = models.JSONField(default=list)

    class Meta:
        ordering = ["-risk_score"]

    def __str__(self):
        return f"{self.full_name} ({self.iin}) — {self.risk_level}"
