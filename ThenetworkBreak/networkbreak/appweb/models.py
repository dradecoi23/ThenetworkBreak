from django.db import models

# Create your models here.

genero_sex = [
    (1, "Hombre"),
    (2, "Mujer")
]


class Persons(models.Model):
    nombre = models.CharField(max_length=30)
    fotos = models.ImageField(upload_to="Fotos", null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    onliFans = models.CharField(max_length=30, blank=True, null=True)
    pagTransmision = models.CharField(max_length=30)
    concursante = models.BooleanField(null=True)
    valor = models.IntegerField(null=True)
    genero = models.IntegerField(
        null=False, blank=False, choices=genero_sex, default=1)

    class Meta:
        ordering = ('-valor',)

    def __str__(self):
        return self.nombre


class ImagenesModelo(models.Model):
    fotos = models.ImageField(upload_to="Fotos")
    modelo = models.ForeignKey(
        Persons, on_delete=models.CASCADE)


class Archivo(models.Model):
    file = models.FileField(upload_to="", null=True)
