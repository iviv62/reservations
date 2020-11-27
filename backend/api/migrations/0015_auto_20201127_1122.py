# Generated by Django 3.1.3 on 2020-11-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20201127_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='day_of_week',
            field=models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
