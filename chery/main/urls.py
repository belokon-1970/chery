from django.urls import path
from . import views, admin

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('kompaniya', views.kompaniya, name='kompaniya'),
    path('modeli', views.modeli, name='modeli'),
    path('opisanie', views.opisanie, name='opisanie'),
    path('calkulete', views.calkulete, name='calkulete'),
    path('arenda', views.arenda, name='arenda'),
]