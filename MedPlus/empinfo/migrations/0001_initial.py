# Generated by Django 4.1.1 on 2023-09-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmpDetailsModels",
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
                ("name", models.CharField(max_length=10)),
                ("age", models.IntegerField()),
                ("height", models.IntegerField()),
                ("weight", models.IntegerField()),
            ],
        ),
    ]
