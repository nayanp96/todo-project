# Generated by Django 4.1.1 on 2022-10-06 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_mytodo_dt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytodo',
            old_name='dt',
            new_name='date_time',
        ),
    ]
