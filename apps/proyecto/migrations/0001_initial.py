# Generated by Django 2.0.5 on 2019-06-10 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionPuestoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoCliente', models.CharField(max_length=10)),
                ('nombreCliente', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=55)),
                ('nit', models.CharField(max_length=15)),
                ('giro', models.CharField(max_length=50)),
                ('numTelefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProyecto', models.CharField(max_length=10)),
                ('nombreProyecto', models.CharField(max_length=25)),
                ('descripcionProyecto', models.CharField(max_length=250)),
                ('ubicacion', models.CharField(max_length=200)),
                ('fechaInicioConstruccion', models.DateField(auto_now_add=True)),
                ('fechaFinalizacion', models.DateField(auto_now_add=True)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoPuesto', models.CharField(max_length=10)),
                ('nombrePuesto', models.CharField(max_length=25)),
                ('descripcionPuesto', models.CharField(max_length=150)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSolicitud', models.DateField(auto_now_add=True)),
                ('solicitante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Puesto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreActividad', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('tiempoEstimado', models.CharField(max_length=35)),
                ('codigoPuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Puesto')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='puestos',
            field=models.ManyToManyField(to='proyecto.Puesto'),
        ),
    ]
