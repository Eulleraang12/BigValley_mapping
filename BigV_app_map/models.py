from django.conf import settings
from django.db import models
from localflavor.br.models  import BRCNPJField, BRPostalCodeField, BRStateField
from phonenumber_field.modelfields import PhoneNumberField

class Dados_Mapeamento(models.Model):
#dados cadastrais
    
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=400, blank=True) 
    email = models.EmailField() 
    cnpj = BRCNPJField(null=True,blank=True) #fazer validação cnpj com js ou jquery

#endereço
    cep = BRPostalCodeField(max_length=9,null=True,blank=True)           #fazer preenchimento automatico 
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)       #fazer como baixa de rolagem                                  
    estado = BRStateField()

#dados do Representante 
    nome_representante = models.CharField(max_length = 20)
    cargo = models.CharField(max_length = 20)
    telefone = PhoneNumberField()
    email_representante = models.EmailField() 

# Características da empresa/startup

    


    def __str__(self):
        return self.nome

    class Meta: 
        verbose_name_plural = "Dados_Mapeamento"

                                              

        



