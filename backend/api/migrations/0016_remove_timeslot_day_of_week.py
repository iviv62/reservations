# Generated by Django 3.1.3 on 2020-11-27 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20201127_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='day_of_week',
        ),
    ]