# Generated by Django 2.0.5 on 2019-06-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
    ]
