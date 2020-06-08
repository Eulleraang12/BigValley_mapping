from django.conf import settings
from django.db import models
import datetime


class Dados_Mapeamento(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14) #fazer validação cnpj
    site = models.URLField(max_length=200) 
    email = models.EmailField()
    # logo = models.ImageField() ### checar a implementação do logo 
    # dt_criacao = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.nome

    class Meta: # tirar o plural do objeto criado no admin
        verbose_name_plural = "Dados_Mapeamento"
   
    # nonlocal nome

class Endereco(models.Model): #### testando pra ver se o forms assim é melhor armazenado
    cep = models.CharField(max_length=100) #fazer preenchimento automatico 
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100) 
    estado = models.CharField(max_length=100) #fazer como baixa de rolagem
    # dt_criacao = models.DateTimeField(auto_now_add = True)


    # def __str__(self):
    #     global nome
    #     return self.nome

    class Meta: # tirar o plural do objeto criado no admin
        verbose_name_plural = "Endereco"


