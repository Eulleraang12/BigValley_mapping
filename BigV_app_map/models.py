from django.conf import settings
from django.db import models
from localflavor.br.models  import BRCNPJField, BRPostalCodeField, BRStateField
from phonenumber_field.modelfields import PhoneNumberField
from .func_lazy import seg_area_lazy,seg_atu_lazy

class Dados_Mapeamento(models.Model):
#dados cadastrais
    
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=400, blank=True) 
    email = models.EmailField() 
    cnpj = BRCNPJField(null=True,blank=True) #fazer validação cnpj com js ou jquery
########################################################################################################################################

#endereço
    cep = BRPostalCodeField(max_length=9,)           #fazer preenchimento automatico 
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)       #fazer como baixa de rolagem                                  
    estado = BRStateField()
########################################################################################################################################

#dados do Representante 
    nome_representante = models.CharField(max_length = 20)
    cargo = models.CharField(max_length = 20)
    telefone = PhoneNumberField(region='BR')
    email_representante = models.EmailField() 
########################################################################################################################################

# Características da empresa/startup
    # segmento de atuação
    industria = models.BooleanField(blank=True)      ##ver se da pra melhorar
    comercio = models.BooleanField(blank=True)
    servico = models.BooleanField(blank=True)

    area_de_atuacao_da_empresa_ou_startup = models.CharField(max_length = 1000)
   
    ##################################################################################
    segArea_CHOICES = ( seg_area_lazy() )
    segmento_area = models.CharField(max_length=6, choices = segArea_CHOICES,default=0)
    ##################################################################################

    detalhes_de_area_de_atuacao = models.CharField(max_length = 1000)

    ##################################################################################
    segAtu_CHOICES = ( seg_atu_lazy() )
    segmento_de_atuacao = models.CharField(max_length=6, choices = segAtu_CHOICES,default=0)
    ##################################################################################
    tipoCliente_CHOICES = (
        ('B2B', 'Empresas e Negócios'),
        ('B2C', 'Consumidores'),
        ('GOV', 'Governo'),
    )
    tipo_de_cliente = models.CharField(max_length=6, choices = tipoCliente_CHOICES,default=0)

########################################################################################################################################


#Questionário 
    merc_Glob_CHOICES = ((True, 'Sim'), (False, 'Não'))
    possui_mercado_Global = models.BooleanField(choices=merc_Glob_CHOICES,default=0)
    ##################################################################################
    inf_militar_CHOICES = ((True, 'Sim'), (False, 'Não'))
    possui_Influencia_ou_interesse_militar =  models.BooleanField(default=0,choices=inf_militar_CHOICES)
    ##################################################################################
    

    
    





    def __str__(self):
        return self.nome

    class Meta: 
        verbose_name_plural = "Dados_Mapeamento"

                                              

        



