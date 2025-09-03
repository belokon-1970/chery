from django.shortcuts import render
from.models import Artiles

def baza_home(request):
    baza = Artiles.objects.all.order_by('-date')
    return render(request, 'baza/baza_home.html', {'baza': baza})