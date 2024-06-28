from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from lliga.models import *

# Create your views here.
def classificacio(request):
    lliga = Lliga.objects.first()
    equips = Equip.objects.all()
    classi = []
 
    # calculem punts en llista de tuples (equip,punts)
    for equip in equips:
        punts = 0
        for partit in lliga.partit_set.filter(local=equip):
            if partit.gols_local() > partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        for partit in lliga.partit_set.filter(visitant=equip):
            if partit.gols_local() < partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        classi.append( (punts,equip.nom_Equip) )
    # ordenem llista
    classi.sort(reverse=True)
    return render(request,"lliga/classificacio.html",
                {
                    "classificacio":classi,
                })


def taula_partits(request):
    lliga = Lliga.objects.first()
    partits = Partit.objects.all().order_by('inici')
    events = Event.objects.all()
    llistapartits = []
 
    # calculem punts en llista de tuples (equip,punts)
        
    for partit in partits:
            elocal=partit.local.nom_Equip
            glocal=partit.gols_local()
            evisitant=partit.visitant.nom_Equip
            gvisitant=partit.gols_visitant()
            data=partit.inici.strftime('%d-%m-%y')
            llistapartits.append( (data,elocal,glocal,evisitant,gvisitant) )

    return render(request,"lliga/taula_partits.html",
                {
                    "llistapartits":llistapartits,
                })
