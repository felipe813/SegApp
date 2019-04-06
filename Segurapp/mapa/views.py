from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from mapa.models import Coordenadas_Poligono
from mapa.models import Barrio
from django.db import models

def index(request):


    barrios = Barrio.objects.all()
    datos = {}
    j=1
    for barrio in barrios:
        datos_barrio = {}
        coordenadas = Coordenadas_Poligono.objects.filter(id_barrio=barrio.id_bario)
        i=2
        #print(barrio.nom_barrio)
        for list in coordenadas:
            datos_barrio[i]=[float(list.latitud),float(list.longitud)]
            i=i+1
        datos_barrio[0]=coordenadas.count()
        datos_barrio[1] = float(barrio.id_bario)
        datos[j]=datos_barrio
        j=j+1
    datos[0]=barrios.count()


    ctx = {"datos": datos}
    return render(request,'index.html',ctx)
