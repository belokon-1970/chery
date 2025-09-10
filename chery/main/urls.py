from django.urls import path
from . import views, admin

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('kompaniya', views.kompaniya, name='kompaniya'),
]