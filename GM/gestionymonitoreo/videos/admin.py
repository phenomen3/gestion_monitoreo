from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Video, Tipo, Folio
from folios.models import Motivo, Submotivo, Ubicacion

class VideoAdmin(admin.ModelAdmin):
    model = Video
    exclude =['creador']

    def folios_relacionados(self, obj):
        folios = obj.folios.all()  # Obtiene la lista de folios relacionados
        folios_links = []
        for folio in folios:
            folio_url = reverse('admin:videos_folio_change', args=[folio.id])  # Reemplaza 'app_name' con el nombre de tu aplicación
            folio_link = format_html('<a href="{}">{}</a>', folio_url, folio)
            folios_links.append(folio_link)
        return format_html("<br>".join(folios_links))
    
    def link_to_video(self, obj):
        video_url = obj.link
        return format_html('<a href="{}" target="_blank">{}</a>', video_url, video_url)

    link_to_video.short_description = 'LINK'

    search_fields = ('titulo', 'folios__folio')
    list_display = ('titulo','link_to_video', 'tipo','fecha', 'folios_relacionados')
    filter_horizontal = ('folios',)
    list_filter = ('tipo', 'fecha')

    

    list_per_page = 20

    

    def save_model(self, request, obj, form, change):
            if not obj.creador:
                obj.creador = request.user
            super().save_model(request, obj, form, change)

class FolioAdmin(admin.ModelAdmin):
    model = Folio

    def c2(self, obj):
        return obj.ubicacion.c2 if obj.ubicacion else ""
    
    c2.short_description = 'C2'

    def alcaldia(self, obj):
        return obj.ubicacion.alcaldia if obj.ubicacion else ""
    
    alcaldia.short_description = 'ALCALDÍA'

    exclude =['creador','videos',]
    list_display = ('folio','motivo' ,'fecha','c2', 'alcaldia')
    search_fields = ('folio__icontains',)
    list_filter = ('fecha','creador',)

    def save_model(self, request, obj, form, change):
            if not obj.creador:
                obj.creador = request.user
            super().save_model(request, obj, form, change)


admin.site.register(Video, VideoAdmin)
admin.site.register(Folio, FolioAdmin)
# admin.site.register(Tipo)