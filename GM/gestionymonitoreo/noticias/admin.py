from django.contrib import admin
from .models import Noticia, Medio, Canal, Estacion, ProgramaRadio, ProgramaTV, RedSocial, Periodico, Tema, Subtema, Tipo, Subtipo, Submotivo, Mencion
from django.contrib.admin import AdminSite

admin.site.site_title = " "
admin.site.site_header = "Gestion y Monitoreo"
admin.site.index_title = 'MIRS'


class NoticiaAdmin(admin.ModelAdmin):
    model = Noticia
    fields = ('titulo', 'descripcion', 'autor_usuario', 'link', 'fecha', 'hora', 'polaridad', 'calificacion', 'tema',
              'subtema', 'tipo', 'subtipo', 'submotivo', 'mencion', 'noticia_principal', 'medio', 'canal', 'estacion',
              'programa_radio', 'programa_tv', 'red_social', 'periodico')
    exclude = ['creador']
    list_display = ('identificador', 'titulo', 'autor_usuario',
                    'descripcion', 'fecha', 'creador')
    list_filter = ('polaridad', 'autor_usuario', 'tema', 'subtema','identificador')
    search_fields = ('titulo', 'descripcion', 'autor_usuario','identificador')
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if not obj.creador:  # Si el creador aún no está establecido
            obj.creador = request.user
        super().save_model(request, obj, form, change)

# class Media:
#     js = ('admin_custom.js',)

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Medio)
admin.site.register(Periodico)
admin.site.register(Canal)
admin.site.register(Estacion)
admin.site.register(ProgramaRadio)
admin.site.register(ProgramaTV)
admin.site.register(RedSocial)
admin.site.register(Tema)
admin.site.register(Subtema)
admin.site.register(Tipo)
admin.site.register(Subtipo)
admin.site.register(Submotivo)
admin.site.register(Mencion)
