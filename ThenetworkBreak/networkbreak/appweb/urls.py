from django.urls import path
from .views import index, profile, tableform, menmodel, womenmodel, editarModelo, eliminarModelo, actualizar,allmodeltop30

urlpatterns = [
    path('', index, name="index"),
    path('profile/<id>/', profile, name="profile"),
    path('tableform/', tableform, name="tableform"),
    path('menmodel/', menmodel, name="menmodel"),
    path('womenmodel/', womenmodel, name="womenmodel"),
    path('editarModelo/<id>/', editarModelo, name="editarModelo"),
    path('eliminarModelo/<id>/', eliminarModelo, name="eliminarModelo"),
    path('actualizar/', actualizar, name="actualizar"),
    path('allmodeltop30/', allmodeltop30, name="allmodeltop30"),
]
