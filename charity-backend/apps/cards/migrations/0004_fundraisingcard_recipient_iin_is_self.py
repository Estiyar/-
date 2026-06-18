from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0003_alter_fundraisingcard_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="fundraisingcard",
            name="is_self",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="fundraisingcard",
            name="recipient_iin",
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
