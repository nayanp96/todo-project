# Generated by Django 4.1.1 on 2022-10-06 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytodo',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
