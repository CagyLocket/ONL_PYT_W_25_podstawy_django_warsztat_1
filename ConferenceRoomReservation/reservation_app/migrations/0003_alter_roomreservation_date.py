# Generated by Django 4.2.1 on 2023-05-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0002_alter_conferenceroom_name_roomreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreservation',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
