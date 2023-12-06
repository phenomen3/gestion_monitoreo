from django.urls import path
from . import views

app_name = 'folios'

urlpatterns = [
    #path('', views.index, name='index'),create/
    path('', views.create_folio, name='create_folio'),
]