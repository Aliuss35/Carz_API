# Generated by Django 5.0.6 on 2024-05-29 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
        ('dealerships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='dealership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealership'),
            preserve_default=False,
        ),
    ]
