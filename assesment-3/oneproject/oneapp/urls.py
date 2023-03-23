from django.contrib import admin
from django.urls import path
from oneapp import views

urlpatterns = [
    path('',views.index),
    path('profile/',views.profile),
    path('updateprofile/',views.updateprofile),
    path('dashboard/',views.dashboard,name='dashboard'),
]
