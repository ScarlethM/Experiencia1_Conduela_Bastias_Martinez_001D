from django import forms
from django.forms import ModelForm
from .models import Reserva, Destino

class ReservaForm(forms.ModelForm):

    class Meta: 
        model= Reserva
        fields = ['idReserva', 'nombreCliente', 'precio', 'destino']
        labels ={
            'idReserva': 'Reserva', 
            'nombreCliente': 'Nombre cliente', 
            'precio': 'Precio', 
            'destino': 'Destino',
        }
        widgets={
            'idReserva': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id reserva', 
                    'id': 'id.Reserva'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del cliente', 
                    'id': 'nombreCliente'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ), 
            'destino': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'destino',
                }
            )

        }

 
    
     