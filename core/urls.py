from django.urls import path
from .views import index, nosotros,galeria,form_reserva,form_mod_reserva,form_de_reserva,ver,registrarse

urlpatterns=[
    path('',index,name='index'),
    path('index',index,name='index'),
    path('nosotros',nosotros, name='nosotros'),
    path('galeria',galeria, name='galeria'),
    path('form_reserva', form_reserva, name='form_reserva'),
    path('form-mod-reserva/<id>', form_mod_reserva, name="form_mod_reserva"),
    path('form-de-reserva/<id>', form_de_reserva, name="form_de_reserva"),
    path('ver', ver, name="ver"),
    path('registrarse', registrarse, name='registrarse'),
]