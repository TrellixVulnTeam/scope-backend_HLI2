# Generated by Django 2.2.13 on 2020-06-22 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individual', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='lose_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 10, 22, 6, 158094)),
        ),
    ]
