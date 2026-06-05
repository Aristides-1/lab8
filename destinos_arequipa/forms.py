from django import forms
from .models import DestinoTuristico


class DestinoTuristicoForm(forms.ModelForm):

    class Meta:
        model = DestinoTuristico

        fields = [
            'nombreCiudad',
            'descripcionCiudad',
            'imagenCiudad',
            'precioTour',
            'ofertaTour'
        ]