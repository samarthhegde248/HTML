# Generated by Django 2.0.1 on 2019-10-13 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serialprac', '0002_auto_20191013_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person',
            field=models.CharField(max_length=20),
        ),
    ]
