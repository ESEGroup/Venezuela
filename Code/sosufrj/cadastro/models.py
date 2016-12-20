from django.db import models

class Usuario(models.Model):
    def __str__(self):
        return (self.cpf_usuario)
    #nome_usuario = models.CharField(max_length=50)
    #idade_usuario = models.IntegerField(default=18)
    cpf_usuario = models.CharField(max_length=12)

class Ocorrencia(models.Model):
    def __str__(self):
        return self.tipo_ocorrencia
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_ocorrencia = models.CharField(max_length=10)
    data_ocorrencia = models.DateTimeField('data de publicacao')
    

# Create your models here.
