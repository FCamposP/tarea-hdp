# Generated by Django 2.0.5 on 2019-06-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructora', '0003_auto_20190613_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='asistencia',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]
