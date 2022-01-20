from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.

def index(request):
    reservas= Reserva.objects.all()
    return render(request,'index.html',context={'datos':reservas})

def nosotros(request):
    return render(request, 'nosotros.html')

def galeria(request):
    return render(request, 'galeria.html')

def registrarse(request):
    return render(request, 'registrarse.html')


def form_reserva(request):
    if request.method=='POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_form.save()
            return redirect('index')
    else:
        reserva_form= ReservaForm()
    return render(request,'core/form_reserva.html',{'reserva_form': reserva_form})

def form_mod_reserva(request,id):
    reserva = Reserva.objects.get(idReserva=id)

    datos ={
        'form': ReservaForm(instance=reserva)
    }
    if request.method == 'POST': 
        formulario = ReservaForm(data=request.POST, instance = reserva)
        if formulario.is_valid: 
            formulario.save()          
            return redirect('ver')
    return render(request, 'core/form_mod_reserva.html', datos)

def ver(request):
    reservas = Reserva.objects.all()

    return render(request, 'core/ver.html', context={'reservas':reservas})

def form_de_reserva(request,id):
    reserva = Reserva.objects.get(idReserva=id)
    reserva.delete()
    return redirect('ver')
def registrarse(request):
    return render(request, 'registrarse.html')