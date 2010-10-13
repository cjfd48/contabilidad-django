# Create your views here.
from django.shortcuts import render_to_response
from obispado.ingresos.models import *
from obispado.aportantes.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Max, Min
import datetime, string

def index(request):
    lista_ultimos_ingresos = Venta.objects.all().order_by('-fecha')[:5]
    return render_to_response('ingresos/index.html', {'lista_ultimos_ingresos': lista_ultimos_ingresos})

def carga(request):
    if 'ap' in request.GET and request.GET['ap']:
        ap = request.GET['ap']
        fe = request.GET['fe']
        ruc = request.GET['ruc']
        if 'tot' in request.GET and request.GET['tot']:
            tot = request.GET['tot']
        else:
            tot = 1000
        #final = ap+fe+ruc+cant+des+pu+ex+tot
        
        
        id_aportante = Aportante.objects.filter(nombre=ap)
        valormaximo = Aportante.objects.aggregate(Max('id'))
        valapmax = valormaximo['id__max']
        valapmax = valapmax + 1
        newingreso = Venta(fecha = fe, aportante_id=1)
        newingreso.save()
        listcant = []
        listdes = []
        listpu = []
        listex = []
        cont = 0
        for i in range(1, 11):
            if 'cant'+str(i) in request.GET and request.GET['cant'+str(i)]:
                listcant.append(request.GET['cant'+str(i)])
                cont = cont + 1
            if 'des'+str(i) in request.GET and request.GET['des'+str(i)]:
                listdes.append(request.GET['des'+str(i)])
            if 'pu'+str(i) in request.GET and request.GET['pu'+str(i)]:
                listpu.append(request.GET['pu'+str(i)])
            if 'ex'+str(i) in request.GET and request.GET['ex'+str(i)]:
                listex.append(request.GET['ex'+str(i)])
            
        
        for i in range(0, cont):
            newventadet = VentaDetalle(venta_id = newingreso.id, cuenta_id = 1, cantidad = listcant[i], exenta = listex[i])
            newventadet.save()
        
        
        #return render_to_response('ingresos/carga_ingreso.html')
        #return HttpResponseRedirect('/carga_ingresos/')
        return render_to_response('ingresos/index.html', {'final': cont})
    return render_to_response('ingresos/carga_ingreso.html')
    
def carga_ingresos(request):
    return render_to_response('ingresos/carga_ingreso.html')