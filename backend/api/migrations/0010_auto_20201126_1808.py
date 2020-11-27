# Generated by Django 3.1.3 on 2020-11-26 17:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201125_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='image',
        ),
        migrations.AddField(
            model_name='account',
            name='badges',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Работа с НЗОК', 'Работа с НЗОК'), ('Обявени цени', 'Обявени цени'), ('Приемане по спешност', 'Приемане по спешност'), ('Работа с деца', 'Работа с деца'), ('Хомеопатия', 'Хомеопатия')], max_length=72),
        ),
    ]