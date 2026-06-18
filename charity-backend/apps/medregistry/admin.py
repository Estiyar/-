from django.contrib import admin

from .models import MedicalDiagnosis, MedicalRecord


class MedicalDiagnosisInline(admin.TabularInline):
    model = MedicalDiagnosis
    extra = 0


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("iin", "full_name", "city", "clinic", "gender")
    search_fields = ("iin", "full_name", "city")
    inlines = [MedicalDiagnosisInline]
