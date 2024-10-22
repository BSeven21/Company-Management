# Generated by Django 4.2.16 on 2024-10-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Testapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="location",
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
                ("l_name", models.CharField(max_length=50)),
                ("l_phone", models.IntegerField()),
                ("l_address", models.TextField()),
            ],
        ),
    ]
