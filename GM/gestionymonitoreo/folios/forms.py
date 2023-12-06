from django import forms
from .models import Folio

class FolioForm(forms.ModelForm):
    class Meta:
        model = Folio
        fields = ['folio_id', 'usuario', 'descripcion', 'colonia']
