from django.shortcuts import render
from .models import Folio
from .forms import FolioForm

def index(request):
    folios = Folio.objects.all().order_by('fecha')
    return render(request, 'folios/index.html', {'folios': folios})

def create_folio(request):
    if request.method == 'POST':
        form = FolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FolioForm()
    return render(request, 'folios/create_folio.html', {'form': form})

