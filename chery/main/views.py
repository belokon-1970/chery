from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html',)

def about(request):
    return render(request, 'main/about.html')

def baza_home(request):
    return render(request, 'main/baza_home.html')

def opisanie(request):
    return render(request, 'main/opisanie.html'),






