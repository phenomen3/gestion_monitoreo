from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Medio(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Medio'
        verbose_name_plural = 'Medios'

    def __str__(self):
        return self.nombre

class Canal(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Canal'
        verbose_name_plural = 'Canales'

    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Estacion'
        verbose_name_plural = 'Estaciones'

    def __str__(self):
        return self.nombre

class ProgramaRadio(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Programa de Radio'
        verbose_name_plural = 'Programas de Radio'

    def __str__(self):
        return self.nombre

class ProgramaTV(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Programa de TV'
        verbose_name_plural = 'Programas de TV'

    def __str__(self):
        return self.nombre

class RedSocial(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        

    def __str__(self):
        return self.nombre

class Periodico(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Periodico'
        verbose_name_plural = 'Periodicos'
    
    def __str__(self):
        return self.nombre

class Tema(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nombre

class Subtema(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Subtema'
        verbose_name_plural = 'Subtemas'


    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nombre
class Subtipo(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Subtipo'
        verbose_name_plural = 'Subtipos'

    def __str__(self):
        return self.nombre

class Submotivo(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Submotivo'
        verbose_name_plural = 'Submotivos'

    def __str__(self):
        return self.nombre

class Mencion(models.Model):
    palabra_clave = models.CharField(max_length=100)
    class Meta:
        ordering = ['palabra_clave']
        verbose_name = 'Mencion'
        verbose_name_plural = 'Menciones'

    def __str__(self):
        return self.palabra_clave

def validate_integer_range(value):
    if value < 1 or value > 5:
        raise ValidationError('La calificación debe estar entre 1 y 5.')

class Noticia(models.Model):
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,blank=True)
    link = models.URLField(blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
    POLARIDAD_CHOICES = [
        ('positivo', 'Positivo'),
        ('neutro', 'Neutro'),
        ('negativo', 'Negativo'),
    ]

    polaridad = models.CharField(max_length=10, choices=POLARIDAD_CHOICES)
    calificacion = models.PositiveIntegerField(validators=[validate_integer_range],
                                               help_text="Ingresa una calificación del 1 al 5.")
    autor_usuario = models.CharField(max_length=100)
    tema = models.ForeignKey(Tema, on_delete=models.DO_NOTHING)
    subtema = models.ForeignKey(Subtema, null=True,blank=True, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING, blank=True, null=True)
    submotivo = models.ForeignKey(Submotivo, null=True, on_delete=models.DO_NOTHING,blank=True)
    subtipo = models.ForeignKey(Subtipo, null=True, on_delete=models.DO_NOTHING,blank=True)
    mencion = models.ForeignKey(Mencion, null=True, on_delete=models.DO_NOTHING,blank=True)
    noticia_principal = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    identificador = models.CharField(max_length=20, unique=True, blank=True, null=True)
    medio = models.ForeignKey(Medio, on_delete=models.DO_NOTHING)
    canal = models.ForeignKey(Canal, on_delete=models.DO_NOTHING, null=True, blank=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.DO_NOTHING, null=True, blank=True)
    programa_radio = models.ForeignKey(ProgramaRadio, on_delete=models.DO_NOTHING, null=True, blank=True)
    programa_tv = models.ForeignKey(ProgramaTV, on_delete=models.DO_NOTHING, null=True, blank=True)
    red_social = models.ForeignKey(RedSocial, on_delete=models.DO_NOTHING, null=True, blank=True)
    periodico = models.ForeignKey(Periodico, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self):
        return self.titulo

    # Define una función para generar el identificador
def generar_identificador(instance):
    noticia_principal = instance.noticia_principal
    if noticia_principal:
        # Obtiene la última noticia relacionada a la noticia principal
        ultima_noticia = Noticia.objects.filter(noticia_principal=noticia_principal).order_by('-identificador').first()
        if ultima_noticia and ultima_noticia.identificador:
            # Obtiene el último número de identificador y agrega uno
            ultimo_numero = int(ultima_noticia.identificador.split('.')[1])
            nuevo_numero = ultimo_numero + 1
        else:
            # Si es la primera noticia relacionada, usa 1 como número de identificador
            nuevo_numero = 1
        # Formatea el identificador con decimales consecutivos
        identificador = f"{noticia_principal.identificador}.{nuevo_numero:02d}"
    else:
        # Si no tiene noticia principal, usa un identificador sin decimales
        identificador = str(instance.id)
    instance.identificador = identificador
    instance.save()

# Crea una señal para generar el identificador después de guardar una noticia
@receiver(post_save, sender=Noticia)
def generar_identificador_noticia(sender, instance, **kwargs):
    if not instance.identificador:
        generar_identificador(instance)

