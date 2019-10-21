# Generated by Django 2.0.1 on 2019-10-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=20)),
                ('leadstatus', models.CharField(max_length=15)),
                ('demodate', models.DateField()),
                ('counsler', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]