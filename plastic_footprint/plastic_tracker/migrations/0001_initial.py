# Generated by Django 3.1.1 on 2020-11-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('id_number', models.IntegerField(blank=True)),
                ('monthly_balance', models.FloatField(default=2.0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('plastic_weight', models.FloatField()),
            ],
        ),
    ]
