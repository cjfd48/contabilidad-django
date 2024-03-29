from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
import datetime, string
import os.path
def index(request):
    user_id = request.user.id
    is_auth = request.user.is_authenticated()
    if(is_auth):
        if request.session.get('has_login',True):
            tipouser = User.objects.get(id=user_id)
            return render_to_response('principal/index.html', {'nombreuser':tipouser.username})
        else:
            return HttpResponseRedirect('/obispado/login/')
    else:
        return HttpResponseRedirect('/obispado/login/')

def ver_logs(request):
    user_id = request.user.id
    is_auth = request.user.is_authenticated()
    listbit = []
    if(is_auth):
        tipouser = User.objects.get(id=user_id)
        nombres = os.listdir("C:/Contabilidad/logs/")
        for x in nombres:
            if x.find("bitacora") >=0:
                listbit.append(x)
        return render_to_response('principal/list_logs.html', {'nombreuser':tipouser.username, 'listbit':listbit, 'cant':'1'})
    else:
        return HttpResponseRedirect('/obispado/login/')