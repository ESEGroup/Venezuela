from django.shortcuts import render
def ocorrencia(request):
    return render(request, 'ocorrencia/ocorrencia.html', {})
