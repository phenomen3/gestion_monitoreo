# Generated by Django 4.2.5 on 2023-10-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folio',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='foliosvideos', to='videos.video'),
        ),
    ]
