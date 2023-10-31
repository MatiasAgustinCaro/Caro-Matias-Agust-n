from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Libro
from .forms import LibroForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

@login_required

def inicio(request):
    return render(request,'paginas/inicio.html')
@login_required
def acerca(request):
    return render(request,'paginas/acerca.html')    

@login_required
def Libros(request):
    Libros= Libro.objects.all()
    return render(request, "libros/index.html", {'libro': Libros})

def crear(request):
  formulario= LibroForm(request.POST or None, request.FILES or None)
  if formulario.is_valid():
     formulario.save()
     return redirect(to='libros')
  return render(request, 'libros/crear.html', {'formulario': formulario} )

def editar(request, id):
  Libros= Libro.objects.get(Id= id)
  formulario = LibroForm(request.POST or None, request.FILES or None, instance=Libros)
  if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect(to='libros')
  return render(request, 'libros/editar.html', {'formulario': formulario})

def borrar(request,  id):
    Libros= Libro.objects.get(Id= id) 
    Libros.delete()
    return redirect(to='libros')

def registro(request):
   data = {
      'form': CustomUserCreationForm()
   }

   if request.method == 'POST':
      form= CustomUserCreationForm(data=request.POST)
      if form.is_valid():
        form.save()
        user= authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
        login(request, user)
        data["form"] = form  
      return redirect(to='Inicio')
   return render (request, 'registration/register.html', data)