# Generated by Django 5.0.6 on 2024-05-16 15:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="experiment",
            old_name="name",
            new_name="dataset",
        ),
    ]