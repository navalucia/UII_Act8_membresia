from django.shortcuts import render, redirect, get_object_or_404
from .models import Membresia

# --- LEER ---
def index(request):
    membresias = Membresia.objects.all()
    return render(request, 'index.html', {'membresias': membresias})

# --- AGREGAR ---
def agregar_membresia(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        costo_mensual = request.POST.get('costo_mensual')
        acceso_limitado = request.POST.get('acceso_limitado') == 'on'
        acceso_entrenador = request.POST.get('acceso_entrenador') == 'on'

        Membresia.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            costo_mensual=costo_mensual,
            acceso_limitado=acceso_limitado,
            acceso_entrenador=acceso_entrenador
        )
        return redirect('inicio')
    return render(request, 'agregar_membresia.html')

# --- EDITAR ---
def editar_membresia(request, id):
    membresia = get_object_or_404(Membresia, id_membresia=id)
    if request.method == 'POST':
        membresia.nombre = request.POST.get('nombre')
        membresia.descripcion = request.POST.get('descripcion')
        membresia.costo_mensual = request.POST.get('costo_mensual')
        membresia.acceso_limitado = request.POST.get('acceso_limitado') == 'on'
        membresia.acceso_entrenador = request.POST.get('acceso_entrenador') == 'on'
        membresia.save()
        return redirect('inicio')
    return render(request, 'editar_membresia.html', {'membresia': membresia})

# --- BORRAR ---
def borrar_membresia(request, id):
    membresia = get_object_or_404(Membresia, id_membresia=id)
    if request.method == 'POST':
        membresia.delete()
        return redirect('inicio')
    return render(request, 'borrar_membresia.html', {'membresia': membresia})
