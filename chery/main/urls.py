from django.urls import path
from . import views, admin

urlpatterns = [
    path('',views.index,),
    path('about111', views.about,),
]
