# Generated by Django 2.0.1 on 2019-10-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0007_auto_20191013_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carservicedetail',
            name='service_date',
            field=models.DateField(auto_now=True),
        ),
    ]
