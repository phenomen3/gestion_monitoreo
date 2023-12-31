# Generated by Django 4.2.5 on 2023-10-04 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import noticias.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Canal',
                'verbose_name_plural': 'Canales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Estacion',
                'verbose_name_plural': 'Estaciones',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Medio',
                'verbose_name_plural': 'Medios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Mencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra_clave', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Mencion',
                'verbose_name_plural': 'Menciones',
                'ordering': ['palabra_clave'],
            },
        ),
        migrations.CreateModel(
            name='Periodico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Periodico',
                'verbose_name_plural': 'Periodicos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ProgramaRadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Programa de Radio',
                'verbose_name_plural': 'Programas de Radio',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ProgramaTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Programa de TV',
                'verbose_name_plural': 'Programas de TV',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Submotivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Submotivo',
                'verbose_name_plural': 'Submotivos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Subtema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subtema',
                'verbose_name_plural': 'Subtemas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Subtipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subtipo',
                'verbose_name_plural': 'Subtipos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('polaridad', models.CharField(choices=[('positivo', 'Positivo'), ('neutro', 'Neutro'), ('negativo', 'Negativo')], max_length=10)),
                ('calificacion', models.PositiveIntegerField(help_text='Ingresa una calificación del 1 al 5.', validators=[noticias.models.validate_integer_range])),
                ('autor_usuario', models.CharField(max_length=100)),
                ('identificador', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('canal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.canal')),
                ('creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.estacion')),
                ('medio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.medio')),
                ('mencion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.mencion')),
                ('noticia_principal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.noticia')),
                ('periodico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.periodico')),
                ('programa_radio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.programaradio')),
                ('programa_tv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.programatv')),
                ('red_social', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.redsocial')),
                ('submotivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.submotivo')),
                ('subtema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.subtema')),
                ('subtipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.subtipo')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.tema')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.tipo')),
            ],
        ),
    ]
