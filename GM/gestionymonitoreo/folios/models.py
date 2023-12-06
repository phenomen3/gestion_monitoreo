import re
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Motivo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Submotivo(models.Model):
    nombre = models.CharField(max_length=100)
    motivo = models.ForeignKey(Motivo, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['nombre']
        verbose_name  = 'Motivo CAD'
        verbose_name_plural = 'Motivos CAD'

    def __str__(self):
        return f"{self.nombre} - {self.motivo} - {self.id}"



def validate_folio_id(value):
    pattern = re.compile(r'^C5/\d{8}/\d+$')
    if not pattern.match(value):
        raise ValidationError('El formato del ID de folio es incorrecto.')


class Folio(models.Model):
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    folio_id = models.CharField(max_length=20, unique=True,
        validators=[validate_folio_id],
        help_text="El formato debe ser C5/yyyymmdd/nnnnn")
    motivo = models.ForeignKey('Submotivo', on_delete=models.DO_NOTHING, null=True, blank=True)
    usuario = models.CharField(max_length=100)  # Campo de usuario como texto
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.folio_id
    class Meta:
        verbose_name = 'Folio'
        verbose_name_plural = 'Folios'
        


class Ubicacion(models.Model):
    c2 = models.CharField(max_length=100, null=True, blank=True)
    alcaldia = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    colonia = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.colonia} ({self.alcaldia})"

    class Meta:
        ordering = ['colonia']
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'