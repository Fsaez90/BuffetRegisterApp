# Generated by Django 4.1 on 2022-12-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest_data',
            name='Registered',
            field=models.BooleanField(default=False),
        ),
    ]
