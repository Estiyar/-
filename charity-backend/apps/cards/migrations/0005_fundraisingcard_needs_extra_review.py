from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0004_fundraisingcard_recipient_iin_is_self"),
    ]

    operations = [
        migrations.AddField(
            model_name="fundraisingcard",
            name="needs_extra_review",
            field=models.BooleanField(default=False),
        ),
    ]
