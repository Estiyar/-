from django.contrib import admin

from .models import FraudProfile


@admin.register(FraudProfile)
class FraudProfileAdmin(admin.ModelAdmin):
    list_display = ("iin", "full_name", "risk_score", "risk_level")
    list_filter = ("risk_level",)
    search_fields = ("iin", "full_name")
