# Generated by Django 4.0.7 on 2022-10-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=25)),
                ('model_price', models.FloatField()),
                ('model_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MobileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=25)),
                ('model_price', models.FloatField()),
                ('model_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TvModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=25)),
                ('model_price', models.FloatField()),
                ('model_qty', models.IntegerField()),
            ],
        ),
    ]
