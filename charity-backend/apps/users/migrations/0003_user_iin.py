from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_platformsettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="iin",
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
