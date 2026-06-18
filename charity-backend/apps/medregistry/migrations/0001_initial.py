from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MedicalRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("iin", models.CharField(max_length=12, unique=True)),
                ("full_name", models.CharField(max_length=255)),
                ("birth_date", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Мужской"), ("female", "Женский")],
                        max_length=8,
                    ),
                ),
                ("city", models.CharField(max_length=128)),
                ("clinic", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="MedicalDiagnosis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("stage", models.CharField(blank=True, max_length=64)),
                ("diagnosed_date", models.DateField()),
                (
                    "record",
                    models.ForeignKey(
                        on_delete=models.deletion.CASCADE,
                        related_name="diagnoses",
                        to="medregistry.medicalrecord",
                    ),
                ),
            ],
            options={
                "ordering": ["-diagnosed_date"],
            },
        ),
    ]
