# Generated by Django 5.0 on 2023-12-12 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submotivo',
            options={'ordering': ['nombre'], 'verbose_name': 'Motivo CAD', 'verbose_name_plural': 'Motivos CAD'},
        ),
        migrations.AlterField(
            model_name='folio',
            name='descripcion',
            field=models.TextField(help_text='Máximo 500 caracteres', max_length=500),
        ),
        migrations.AlterField(
            model_name='folio',
            name='usuario',
            field=models.CharField(max_length=50),
        ),
    ]