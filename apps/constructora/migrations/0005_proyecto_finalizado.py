# Generated by Django 2.0.5 on 2019-06-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructora', '0004_auto_20190613_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]