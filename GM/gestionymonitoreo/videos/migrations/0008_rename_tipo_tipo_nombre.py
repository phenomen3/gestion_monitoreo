# Generated by Django 4.2.5 on 2023-10-13 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_rename_nombre_tipo_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo',
            old_name='tipo',
            new_name='nombre',
        ),
    ]
