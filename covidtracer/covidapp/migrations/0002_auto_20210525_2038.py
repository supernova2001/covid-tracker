# Generated by Django 3.1.7 on 2021-05-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oxygen',
            name='Agencyphonenumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='verification',
            field=models.CharField(max_length=3),
        ),
    ]
