# Generated by Django 4.2.5 on 2023-10-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospitalapp", "0005_alter_patientreports_db_patientid"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient_db",
            name="date",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]