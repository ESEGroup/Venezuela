from django.http import HttpResponse
from django.template import  loader

from .models import Ocorrencia

def campos(request):
    ultimas_ocorrencias = Ocorrencia.objects.order_by('-data_ocorrencia')[:3]
    output = ', '.join ([o.tipo_ocorrencia for o in ultimas_ocorrencias])
    return HttpResponse(output)

def protocolo(request):
    return HttpResponse("aqui seria o protocolo da sua ocorrencia.")

# Create your views here.
