from django import forms
from .models import Folio

class TextoLargoWidget(forms.Textarea):
    def _init_(self, attrs=None):
        default_attrs = {'rows': 3, 'style': 'overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-height: 3.6em;'}
        if attrs:
            default_attrs.update(attrs)
        super()._init_(default_attrs)
        #return default_attrs

class FolioForm(forms.ModelForm):
    class Meta:
        model = Folio
        fields = ['folio_id', 'usuario', 'descripcion']
        #fields = ['folio_id', 'usuario', 'descripcion', 'colonia'] se elimino 'colonia' por el error: File "/home/mic5/monitoreoygestion/gestion_monitoreo/mento/lib/python3.10/site-packages/django/forms/models.py", line 331, in __new__
        # raise FieldError(message)
        # django.core.exceptions.FieldError: Unknown field(s) ( colonia) specified for Folio

