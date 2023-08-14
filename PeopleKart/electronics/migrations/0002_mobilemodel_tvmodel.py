# Generated by Django 4.1.1 on 2023-08-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electronics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MobileModel",
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
                ("mname", models.CharField(max_length=25)),
                ("mprice", models.IntegerField()),
                ("mqty", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TvModel",
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
                ("mname", models.CharField(max_length=25)),
                ("mprice", models.IntegerField()),
                ("mqty", models.IntegerField()),
            ],
        ),
    ]