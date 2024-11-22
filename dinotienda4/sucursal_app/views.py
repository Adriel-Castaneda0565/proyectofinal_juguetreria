from django.shortcuts import render,redirect
from .models import Sucursal
# Create your views here.
def inicio_vista(request):
    lasucursal=Sucursal.objects.all()

    return render(request, 'gestionarSucursal.html', {'misucursal':lasucursal})

def registrarSucursal(request):
    id_suc=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdir"]
    telefono=request.POST["txttelf"]
    email=request.POST["txtemail"]
    horario=request.POST["txthora"]
    CP=request.POST["txtcp"]
    web=request.POST["txtweb"]
    guardarSucursal=Sucursal.objects.create(id_suc=id_suc,nombre=nombre,direccion=direccion,telefono=telefono,email=email,horario=horario,CP=CP,web=web)
    return redirect('/')

def seleccionarSucursal(request,id_suc):
    Sucu=Sucursal.objects.get(id_suc=id_suc)
    return render(request,"editarSucursal.html",{'misucursal':Sucu})

def editarSucursal(request):
    id_suc=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdir"]
    telefono=request.POST["txttelf"]
    email=request.POST["txtemail"]
    horario=request.POST["txthora"]
    CP=request.POST["txtcp"]
    web=request.POST["txtweb"]
    Sucu=Sucursal.objects.get(id_suc=id_suc)
    Sucu.nombre=nombre
    Sucu.direccion=direccion
    Sucu.telefono=telefono
    Sucu.email=email
    Sucu.horario=horario
    Sucu.CP=CP
    Sucu.web=web
    
    Sucu.save()
    return redirect('/')

def borrarSucursal(request,id_suc):
    Sucu=Sucursal.objects.get(id_suc=id_suc)
    Sucu.delete()
    return redirect('/')