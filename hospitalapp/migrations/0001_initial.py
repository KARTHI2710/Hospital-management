# Generated by Django 4.2.5 on 2023-10-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pathologist_db",
            fields=[
                (
                    "Doctorcode",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("DoctorName", models.CharField(max_length=20)),
                ("Specialization", models.CharField(max_length=20)),
                ("Address", models.CharField(max_length=50)),
                ("Qualification", models.CharField(max_length=10)),
                ("Mobile", models.IntegerField()),
                ("Signature", models.ImageField(blank=True, upload_to="signature/")),
            ],
        ),
        migrations.CreateModel(
            name="Patient_db",
            fields=[
                (
                    "uhid",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=10)),
                ("patientname", models.CharField(max_length=10)),
                ("gender", models.CharField(max_length=10)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.IntegerField()),
                ("refdr", models.CharField(max_length=20)),
                ("selected_test", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Refdr_db",
            fields=[
                (
                    "Doctorcode",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("DoctorName", models.CharField(max_length=20)),
                ("Specialization", models.CharField(max_length=20)),
                ("Address", models.CharField(max_length=50)),
                ("Qualification", models.CharField(max_length=10)),
                ("Mobile", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Report_db",
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
                ("Reportcode", models.IntegerField()),
                ("ReportName", models.CharField(max_length=20)),
                ("Template", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Test_db",
            fields=[
                (
                    "Testcode",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("TestName", models.CharField(max_length=20)),
                ("speicmentype", models.CharField(max_length=20)),
            ],
        ),
    ]