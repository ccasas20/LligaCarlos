from django.urls import path

from . import views

urlpatterns = [
    path("classificacio/", views.classificacio, name="classificacio"),
    path("taula/", views.taula_partits, name="taula_partits"),
]

