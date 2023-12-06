from django.contrib import admin
from .models import Ubicacion, Motivo, Submotivo, Folio


class FolioAdmin(admin.ModelAdmin):
    model = Folio
    fields = ('folio_id', 'motivo', 'usuario', 'descripcion', 'fecha', 'hora', 'ubicacion')
    exclude = ['creador']
    list_display = ( 'folio_id', 'motivo', 'usuario', 'descripcion', 'fecha', 'ubicacion', 'nombre_sector', 'creador',)
    def nombre_sector(self, obj):
        return obj.ubicacion.sector  # Accedemos al campo 'sector' del modelo relacionado

    nombre_sector.short_description = 'Sector'
    list_filter = ('creador', 'fecha')  # Deja solo los campos apropiados para filtrar
    search_fields = ('motivo__nombre', 'descripcion', 'usuario')

    

    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if not obj.creador:  # Si el creador aún no está establecido
            obj.creador = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Folio, FolioAdmin)
# admin.site.register(Motivo)
admin.site.register(Submotivo)
admin.site.register(Ubicacion)
# admin.site.register(Alcaldia)
# admin.site.register(C2)
# admin.site.register(Sector)

