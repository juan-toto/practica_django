from django.shortcuts import render
from .models import Servicio

# Create your views here.

def servicios(request):
    ser = Servicio.objects.all()
    return render(request,'servicios/servicios.html', {'ser':ser})