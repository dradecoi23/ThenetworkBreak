from django.contrib import admin
from .models import Persons, ImagenesModelo
# Register your models here.


class ImagenesModeloAdmin(admin.StackedInline):
    model = ImagenesModelo


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    inlines = [
        ImagenesModeloAdmin
    ]

    class Meta:
        model = Persons


@admin.register(ImagenesModelo)
class ImagenesModeloAdmin(admin.ModelAdmin):
    pass
