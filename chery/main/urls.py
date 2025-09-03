from django.urls import path
from . import views, admin

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('modeli', views.modeli, name='modeli'),
]