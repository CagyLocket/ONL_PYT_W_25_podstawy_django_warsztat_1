# Generated by Django 4.2.1 on 2023-05-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0003_alter_roomreservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreservation',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
