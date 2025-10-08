from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html',)

def about(request):
    return render(request, 'main/about.html')

def kompaniya(request):
    return render(request, 'main/kompaniya.html')

def baza_home(request):
    return render(request, 'main/baza_home.html')

def modeli(request):
    return render(request, 'main/modeli.html')

def opisanie(request):
    return render(request, 'main/opisanie.html')

def calkulete(request):
    return render(request, 'main/calkulete.html')

def arenda(request):
    return render(request, 'main/arenda.html')





