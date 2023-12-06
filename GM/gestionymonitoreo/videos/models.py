from django.db import models
from django.contrib.auth.models import User
from folios.models import Motivo, Submotivo, Ubicacion


class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nombre


class Folio(models.Model):
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='creadorvideos')
    folio = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.DO_NOTHING,related_name='ubicacionfoliosvideos', null=True, blank=True) 
    motivo = models.ForeignKey(Submotivo, on_delete=models.DO_NOTHING, null=True, blank=True,related_name='motivovideos')
    videos = models.ManyToManyField('Video', related_name='foliosvideos')
    class Meta:
        ordering = ['fecha']
        verbose_name = 'Folio'
        verbose_name_plural = 'Folios'


    def __str__(self):
        return self.folio

class Video(models.Model):
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    tipo =  models.ForeignKey(Tipo, on_delete=models.DO_NOTHING, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    folios = models.ManyToManyField(Folio)  

    class Meta:
        ordering = ['fecha']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.titulo