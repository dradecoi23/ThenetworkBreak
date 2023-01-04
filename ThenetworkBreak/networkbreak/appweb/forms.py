from dataclasses import field
from logging import PlaceHolder
from django import forms
from .models import Persons, ImagenesModelo


class FormularioForm(forms.ModelForm):

    class Meta:
        model = Persons
        fields = ["nombre", "fotos", "instagram",
                  "onliFans", "pagTransmision", "genero"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fotos"].widget.attrs.update({"class": "site-btn"})
        self.fields["genero"].widget.attrs.update({"class": "site-btn"})
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                PlaceHolder=f'{str(field)}')
            self.fields[str(field)].label = ''


class ImagenesModeloForm(forms.ModelForm):

    class Meta:
        model = ImagenesModelo
        fields = ["fotos"
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fotos"].widget.attrs.update({"class": "site-btn"})
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                PlaceHolder=f'{str(field)}')
            self.fields[str(field)].label = ''
