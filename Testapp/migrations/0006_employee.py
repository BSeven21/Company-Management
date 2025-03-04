# Generated by Django 4.2.16 on 2024-10-18 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Testapp", "0005_remove_location_l_company_location_l_com_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("e_name", models.CharField(max_length=255)),
                ("e_phone", models.CharField(max_length=20)),
                ("e_address", models.CharField(max_length=255)),
                (
                    "e_com",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Testapp.company",
                    ),
                ),
                (
                    "e_loc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Testapp.location",
                    ),
                ),
            ],
        ),
    ]
