from django.http import HttpResponse
from django.shortcuts import render
from django.template import  loader

from .models import Ocorrencia

def campos(request):
    ultimas_ocorrencias = Ocorrencia.objects.order_by('-data_ocorrencia')[:3]
    context = {
        'ultimas_ocorrencias': ultimas_ocorrencias,
    }
    return render(request, 'cadastro/campos.html', context)

def protocolo(request):
    return HttpResponse("aqui seria o protocolo da sua ocorrencia.")

# Create your views here.


