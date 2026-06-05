from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.index,
        name="index"
    ),

    path(
        "crear/",
        views.crear_destino,
        name="crear_destino"
    ),

    path(
        "editar/<int:id>/",
        views.editar_destino,
        name="editar_destino"
    ),

    path(
        "eliminar/<int:id>/",
        views.eliminar_destino,
        name="eliminar_destino"
    ),

]