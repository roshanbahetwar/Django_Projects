# Generated by Django 4.1.1 on 2023-07-11 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("actress", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="actressdetailsmodels", old_name="age", new_name="a_age",
        ),
        migrations.RenameField(
            model_name="actressdetailsmodels", old_name="city", new_name="a_city",
        ),
        migrations.RenameField(
            model_name="actressdetailsmodels", old_name="name", new_name="a_name",
        ),
        migrations.RenameField(
            model_name="actressdetailsmodels", old_name="salary", new_name="a_salary",
        ),
        migrations.RemoveField(model_name="actressdetailsmodels", name="email",),
    ]
