from django.shortcuts import render
from django.urls import path
from . import views 

urlpatterns =[
    path ("", views.index, name="index"),
    path ("<int:id>/", views.detail, name="index"),
    path ("<int:id>/results", views.results, name="index"),
    path ("<int:id>/vote", views.vote, name="index"),
]