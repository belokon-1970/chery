from django.urls import path
from . import views, admin

urlpatterns = [
    path('',views.baza_home, name='baza_home'),

]