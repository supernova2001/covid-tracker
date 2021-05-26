# Generated by Django 3.1.7 on 2021-05-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0003_auto_20210526_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=10000000)),
                ('address', models.CharField(max_length=100000000)),
                ('number', models.CharField(max_length=10)),
                ('googlemaplink', models.CharField(max_length=1000000000000000000)),
                ('verified', models.CharField(max_length=4)),
            ],
        ),
    ]
