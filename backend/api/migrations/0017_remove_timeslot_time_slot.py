# Generated by Django 3.1.3 on 2020-11-27 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20201127_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='time_slot',
        ),
    ]
