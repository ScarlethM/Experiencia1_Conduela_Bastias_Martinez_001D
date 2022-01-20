from django.db import models

# Create your models here.

#Modelo para Destino
class Destino(models.Model):
    idDestino = models.IntegerField(primary_key=True, verbose_name='Id de Destino')
    nombreDestino = models.CharField(max_length=60, verbose_name='Nombre Destino')

    def __str__(self):
        return self.nombreDestino

#Modelo para Reserva

class Reserva(models.Model):
    idReserva = models.IntegerField(max_length=5, primary_key=True, verbose_name='Nro Reserva')
    nombreCliente = models.CharField(max_length=60, verbose_name='Nombre Cliente')
    precio = models.IntegerField(max_length=7, verbose_name='Precio')
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCliente




