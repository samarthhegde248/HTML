# Generated by Django 2.0.1 on 2019-10-11 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.TextField(max_length=150)),
                ('cost', models.IntegerField()),
                ('no_of_products', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('account_balance', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='buyproduct',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.User'),
        ),
        migrations.AddField(
            model_name='buyproduct',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Product'),
        ),
    ]
