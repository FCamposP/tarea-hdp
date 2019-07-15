# Generated by Django 2.0.5 on 2019-07-15 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionHerramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsignacion', models.DateField(auto_now_add=True)),
                ('fechaDisponible', models.DateField(auto_now_add=True)),
                ('cantidadAsignada', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionoEjemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsignacion', models.DateField(auto_now_add=True)),
                ('fechaDisponible', models.DateField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionPuestoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(max_length=25)),
                ('descripcion_tipo_usuario', models.CharField(max_length=150)),
                ('empleado_proyecto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='constructora.AsignacionPuestoProyecto')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsistencia', models.DateField(auto_now_add=True)),
                ('asistencia', models.BooleanField(default=True)),
                ('Asignacion', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='constructora.AsignacionPuestoProyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoCliente', models.CharField(max_length=10)),
                ('nombreCliente', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=30)),
                ('nit', models.CharField(max_length=14)),
                ('giro', models.CharField(max_length=50)),
                ('numTelefono', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fechaContratacion', models.DateField(auto_now_add=True)),
                ('periodoContrato', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiporecurso', models.CharField(max_length=150)),
                ('recurso', models.CharField(max_length=150)),
                ('cantidad', models.IntegerField(default=0)),
                ('asignado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('codigoEjemplar', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombreEjemplar', models.CharField(max_length=25)),
                ('descripcionEjemplar', models.CharField(max_length=100)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=250)),
                ('numTelefono', models.CharField(max_length=8)),
                ('dui', models.CharField(max_length=9)),
                ('nit', models.CharField(max_length=14)),
                ('isss', models.CharField(max_length=15)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('codigoHerramienta', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombreHerramienta', models.CharField(max_length=15)),
                ('cantidadHerramienta', models.IntegerField(default=0)),
                ('canatidadDisponibles', models.IntegerField(default=0)),
                ('descripcionHerramienta', models.CharField(max_length=100)),
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
                ('fechaInicioConstruccion', models.DateField(null=True)),
                ('fechaFinalizacion', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoPuesto', models.CharField(max_length=10)),
                ('nombrePuesto', models.CharField(max_length=25)),
                ('descripcionPuesto', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('codigoRecurso', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombreRecurso', models.CharField(max_length=25)),
                ('tipoRecurso', models.CharField(max_length=20)),
                ('descripcionRecurso', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSolicitud', models.DateField(auto_now_add=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.AsignacionPuestoProyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreActividad', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('tiempoEstimado', models.CharField(max_length=35)),
                ('codigoPuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Puesto')),
            ],
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='idRecurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Recurso'),
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Solicitud'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Empleado'),
        ),
        migrations.AddField(
            model_name='asignacionpuestoproyecto',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Empleado'),
        ),
        migrations.AddField(
            model_name='asignacionpuestoproyecto',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Proyecto'),
        ),
        migrations.AddField(
            model_name='asignacionpuestoproyecto',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Puesto'),
        ),
        migrations.AddField(
            model_name='asignacionoejemplar',
            name='ejemplar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Ejemplar'),
        ),
        migrations.AddField(
            model_name='asignacionoejemplar',
            name='idProyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Proyecto'),
        ),
        migrations.AddField(
            model_name='asignacionherramienta',
            name='Herramienta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Herramienta'),
        ),
        migrations.AddField(
            model_name='asignacionherramienta',
            name='idProyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructora.Proyecto'),
        ),
    ]
