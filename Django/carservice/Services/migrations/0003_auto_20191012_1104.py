# Generated by Django 2.0.1 on 2019-10-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_auto_20191011_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerdetails',
            name='dob',
            field=models.CharField(max_length=10),
        ),
    ]
