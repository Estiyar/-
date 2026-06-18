from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FraudProfile",
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
                ("risk_score", models.PositiveSmallIntegerField()),
                (
                    "risk_level",
                    models.CharField(
                        choices=[
                            ("low", "Низкий"),
                            ("medium", "Средний"),
                            ("high", "Высокий"),
                        ],
                        max_length=8,
                    ),
                ),
                ("reasons", models.JSONField(default=list)),
            ],
            options={
                "ordering": ["-risk_score"],
            },
        ),
    ]
