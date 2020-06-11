from django.conf import settings
from django.db import models
from django.contrib.localflavor.br.models  import BRCNPJField, BRPostalCodeField
from threading import local




class Dados_Mapeamento(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=400, blank=True) 

    email = models.EmailField() 

    cnpj = BRCNPJField(null=True,blank=True) #fazer validação cnpj

    def __str__(self):
        return self.nome

    class Meta: # tirar o plural do objeto criado no admin
        verbose_name_plural = "Dados_Mapeamento"
    
    

class Endereco(models.Model): #### testando pra ver se o forms assim é melhor armazenado
    cep = BRPostalCodeField(max_length=9)                                                       #fazer preenchimento automatico 
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100) 
    estado = models.CharField(max_length=100)                                                   #fazer como baixa de rolagem
    
    def __str__(self): #melhorar isso 
        return self.cep 
        
    class Meta: # tirar o plural do objeto criado no admin
        verbose_name_plural = "Endereco"



