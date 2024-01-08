from django.contrib import admin
from .models import Ubicacion, Motivo, Submotivo, Folio
#from django.db import models 
#from .forms import TextoLargoWidget
#from django import forms

# class TextoLargoWidgetAdmin(admin.ModelAdmin):
#     form = TextoLargoWidget

class FolioAdmin(admin.ModelAdmin):
    
    
    model = Folio
    # formfield_overrides = { 
    #     models.TextField: {'widget': TextoLargoWidget},
    # }


    fields = ('folio_id', 'motivo', 'usuario', 'descripcion', 'fecha', 'hora', 'ubicacion')
    exclude = ['creador']
    list_display = ('folio_id', 'motivo', 'usuario', 'descripcion_corta', 'fecha', 'ubicacion', 'nombre_sector', 'creador',)
    # ordering = ['fecha']
    def nombre_sector(self, obj):
        return obj.ubicacion.sector  # Accedemos al campo 'sector' del modelo relacionado

    def descripcion_corta(self, obj): # metodo para acortar la descripcion a mostrar
        print("Ingreso el metodo")
        
        max_lines = 3
        lines = obj.descripcion.splitlines()[:max_lines]
        truncated_description = '\n'.join(lines)

        max_length = 60  # Puedes ajustar este valor según tu preferencia
        if len(truncated_description) > max_length:
            truncated_description = f"{truncated_description[:max_length]}..."
        
        return truncated_description

    nombre_sector.short_description = 'Sector'
    descripcion_corta.short_description = 'Descripción Corta'
    #descripcion.short_description = 'descripcion'
    list_filter = ('creador', 'fecha')  # Deja solo los campos apropiados para filtrar
    search_fields = ('folio_id','motivo__nombre', 'descripcion', 'usuario')


    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if not obj.creador:  # Si el creador aún no está establecido
            obj.creador = request.user
        super().save_model(request, obj, form, change)

class SubmotivoAdmin(admin.ModelAdmin):
    model = Submotivo
    fields=('nombre', 'motivo','id')
    list_display = ('nombre', 'motivo', 'id')
    search_fields = ('motivo__nombre','nombre')
    # Submotivo.objects.filter(autor__nombre__icontains="Smith")

admin.site.register(Folio, FolioAdmin)
admin.site.register(Motivo)
admin.site.register(Submotivo, SubmotivoAdmin)
admin.site.register(Ubicacion)
#admin.site.register(TextoLargoWidget, TextoLargoWidgetAdmin)
# admin.site.register(Alcaldia)
# admin.site.register(C2)
# admin.site.register(Sector)

