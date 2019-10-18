# Generated by Django 2.0.1 on 2019-10-13 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serialprac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(default='samarth', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='music_library',
            name='person',
            field=models.ForeignKey(default='samarth', on_delete=django.db.models.deletion.CASCADE, to='serialprac.person'),
            preserve_default=False,
        ),
    ]
