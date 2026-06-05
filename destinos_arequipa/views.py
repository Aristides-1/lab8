from django.shortcuts import render, redirect, get_object_or_404

from .models import DestinoTuristico
from .forms import DestinoTuristicoForm


def index(request):

    destinos = DestinoTuristico.objects.all()

    return render(
        request,
        "index.html",
        {
            "destinos": destinos
        }
    )


def crear_destino(request):

    if request.method == "POST":

        form = DestinoTuristicoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("index")

    else:

        form = DestinoTuristicoForm()

    return render(
        request,
        "form_destino.html",
        {
            "form": form,
            "titulo": "Agregar Destino"
        }
    )


def editar_destino(request, id):

    destino = get_object_or_404(
        DestinoTuristico,
        id=id
    )

    if request.method == "POST":

        form = DestinoTuristicoForm(
            request.POST,
            request.FILES,
            instance=destino
        )

        if form.is_valid():
            form.save()
            return redirect("index")

    else:

        form = DestinoTuristicoForm(
            instance=destino
        )

    return render(
        request,
        "form_destino.html",
        {
            "form": form,
            "titulo": "Editar Destino"
        }
    )


def eliminar_destino(request, id):

    destino = get_object_or_404(
        DestinoTuristico,
        id=id
    )

    destino.delete()

    return redirect("index")