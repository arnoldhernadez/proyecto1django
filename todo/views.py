from django.shortcuts import render,redirect
from .models import Tarea
from .forms import TareaForm


def home(request):
    tareas=Tarea.objects.all()
    context={'tareas':tareas}
    return render(request, 'home.html',context)

def agregar(request):
    if request.method=="POST2":
        form= TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TareaForm()
        context={'form':form}
    return render(request, 'agregar.html', context)

def eliminar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    return redirect("home")
    
        