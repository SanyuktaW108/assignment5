from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('newrecord/',views.registration,name='registration'),
    path('adddata/',views.savedata,name='savedata')

]