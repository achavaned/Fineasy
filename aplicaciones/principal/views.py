from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from django.http import  HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.

from .models import Ingreso, Gasto
from .form import *
from .filters import *
from itertools import chain

@login_required(login_url='login') 
def home(request):
    ingresos = Ingreso.objects.filter(usuario=request.user)
    gastos = Gasto.objects.filter(usuario=request.user)
    gastos_totales = 0
    ingresos_totales = 0
    saldo = 0
    for e in ingresos:
        ingresos_totales += e.valor
    for e in gastos:
        gastos_totales += e.valor
    saldo = ingresos_totales - gastos_totales
    return render(request, "principal/home.html", {'ingresos':ingresos,'gastos':gastos, "saldo":saldo})

@login_required(login_url='login') 
def calendar(request):
    ingresos = Ingreso.objects.filter(usuario=request.user)
    gastos = Gasto.objects.filter(usuario=request.user)
    
    #result_list = list(chain(ingresos, gastos))
    myIngresosFilter = CalendarIngresosFilter(request.GET, queryset=ingresos)
    ingresos=myIngresosFilter.qs 
    myGastosFilter = CalendarGastosFilter(request.GET, queryset=gastos)
    gastos=myGastosFilter.qs 
    
    return render(request, "principal/calendar.html", {'ingresos':ingresos,'gastos':gastos, 'myIngresosFilter':myIngresosFilter, 'myGastosFilter':myGastosFilter})

@login_required(login_url='login') 
def ingresos(request):
    ingresos = Ingreso.objects.filter(usuario=request.user)
    myTagIngresosFilter = TipoIngresosFilter(request.GET, queryset=ingresos)
    ingresos=myTagIngresosFilter.qs 
    return render(request, "principal/ingresos.html", {'ingresos':ingresos, 'myTagIngresosFilter':TipoIngresosFilter})

@login_required(login_url='login') 
def gasto(request):
    gastos = Gasto.objects.filter(usuario=request.user)
    myTagGastosFilter = TipoGastosFilter(request.GET, queryset=gastos)
    gastos=myTagGastosFilter.qs
    return render(request, "principal/gasto.html", {'gastos':gastos, 'myTagGastosFilter':TipoGastosFilter})

@login_required(login_url='login') 
def config(request):
    return render(request, "principal/config.html")



def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,"Username OR password is incorrect")
        context = {}
        return render(request,"principal/login.html",context)



    #registro
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'La cuenta: ' + user + ' ha sido creada')
                email = form.cleaned_data.get('email')
                send_mail('Felicitaciones por su registro!', 'Gracias por hacer parte de Fineasy, disfrute su experiencia','fineasy1@gmail.com', [email],fail_silently=False)
                return redirect('login')


        context = {'form' : form}
        return render(request, "principal/register.html",context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def crearIngreso(request):
    form = IngresoForm()
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user
            instance.save()
            return redirect('/ingresos')
    context = {'form':form}
    return render(request,'principal/agregarIngreso.html', context)

def crearGasto(request):
    form = GastoForm()
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user
            instance.save()
            return redirect('/gasto')
    context ={'form':form}
    return render(request,'principal/agregarGasto.html', context)

def updateIngreso(request,pk):
    ingreso = Ingreso.objects.get(id=pk)
    form = IngresoForm(instance=ingreso)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('/ingresos')
    context ={'form':form}
    return render(request,'principal/agregarIngreso.html', context)

def updateGasto(request,pk):
    gasto = Gasto.objects.get(id = pk)
    form = GastoForm(instance=gasto)
    if request.method == 'POST':
        form = GastoForm(request.POST,instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('/gasto')
    context ={'form':form}
    return render(request,'principal/agregarGasto.html', context)

def deleteIngreso(request,pk):
    ingreso = Ingreso.objects.get(id=pk)
    if request.method == 'POST':
        ingreso.delete()
        return redirect('/ingresos')
    context = {'item':ingreso}
    return render(request, 'principal/deleteIngreso.html', context )

def deleteGasto(request,pk):
    gasto = Gasto.objects.get(id = pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('/gasto')
    context = {'item':gasto}
    return render(request, 'principal/deleteGasto.html', context )
def config(request):
    form = Profile(instance=request.user)
    if request.method == 'POST':
        form = Profile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'principal/config.html',context)
def ingresosChart(request):
    labels = []
    data = []
    ingresos = Ingreso.objects.filter(usuario=request.user).order_by('valor')
    for ingreso in ingresos:
        labels.append(ingreso.nombre_ingreso)
        data.append(ingreso.valor)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
def gastosChart(request):
    labels = []
    data = []
    gastos = Gasto.objects.filter(usuario=request.user).order_by('valor')
    for gasto in gastos:
        labels.append(gasto.nombre_Gasto)
        data.append(gasto.valor)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
