# Generated by Django 5.0.4 on 2024-04-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pslvisapp", "0002_data_data_field_data_session_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="data_field",
            field=models.JSONField(default=list),
        ),
    ]