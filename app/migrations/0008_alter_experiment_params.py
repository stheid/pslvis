# Generated by Django 5.0.6 on 2024-07-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_experiment_params"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experiment",
            name="params",
            field=models.JSONField(
                blank=True, default=dict, verbose_name="Additional Experient Parameters"
            ),
        ),
    ]