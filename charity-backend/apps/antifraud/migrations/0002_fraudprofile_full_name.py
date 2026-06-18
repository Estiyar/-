from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("antifraud", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fraudprofile",
            name="full_name",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
