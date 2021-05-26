from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.showView,name="home"),
    path('home/oxygen',views.OxygenView,name="oxygen"),
    path('oxygen-form/',views.SubmitOxygen,name="oxygen-form"),
    path('home/pharmacies',views.Pharmacies,name="pharmacies")
]
