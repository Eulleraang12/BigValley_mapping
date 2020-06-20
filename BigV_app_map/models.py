from django.conf import settings
from django.db import models


from localflavor.br.models  import BRCNPJField, BRPostalCodeField, BRStateField
from phonenumber_field.modelfields import PhoneNumberField
from .func_lazy import seg_area_lazy,seg_atu_lazy,receita_lazy
from multiselectfield import MultiSelectField #salvou minha vida 

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
    estado = BRStateField(default=0)
########################################################################################################################################

#dados do Representante 
    nome_representante = models.CharField(max_length = 20)
    cargo = models.CharField(max_length = 20)
    telefone = PhoneNumberField(region='BR')
    email_representante = models.EmailField() 
########################################################################################################################################

# Características da empresa/startup


    setor_de_atuaca_CHOICES = (
        ("ind", 'Indústria'),
        ("com", 'Comércio'),
        ("ser", 'Serviços'),
    )

    setor_de_atuacao = MultiSelectField(choices = setor_de_atuaca_CHOICES)

    ##################################################################################

    area_de_atuacao_da_empresa_ou_startup = models.CharField(max_length = 1000)
   
    ##################################################################################
    segArea_CHOICES = ( 
                        seg_area_lazy() 
    
                    )

    segmento_area = models.CharField(max_length=3, choices = segArea_CHOICES,default=3)
    ##################################################################################

    detalhes_de_area_de_atuacao = models.CharField(max_length = 1000)

    ##################################################################################
    segAtu_CHOICES = ( 
                        seg_atu_lazy() 
                    )

    segmento_de_atuacao = models.CharField(max_length=3, choices = segAtu_CHOICES,default=3)
    ##################################################################################
    tipoCliente_CHOICES = (
        ('B2B', 'Empresas e Negócios (B2B) '),
        ('B2C', 'Consumidores (B2C) '),
        ('GOV', 'Governo'),
    )
    tipo_de_cliente = models.CharField(max_length=3, choices = tipoCliente_CHOICES,default=3)

########################################################################################################################################


#Questionário 
    sim_nao_CHOICES = ((True, 'Sim'), (False, 'Não'))

    possui_mercado_Global = models.BooleanField(choices=sim_nao_CHOICES,default=3)

    possui_Influencia_ou_interesse_militar =  models.BooleanField(default=0,choices=sim_nao_CHOICES)
    ##################################################################################

    saida_neg_CHOICES = (
                        ('cre','Crescimento Lucrativo para o Mercado Global '),
                        ('aqu','Aquisição por uma Grande Empresa'),
                        ('fus','Fusão com outra empresa'),
                        ('ofe','Oferta Pública Inicial de Ações'),
            )
    qual_estrategia_de_saida_ou_idealizada_para_o_negocio = MultiSelectField(choices=saida_neg_CHOICES,default=0)

    ##################################################################################

    possui_CHOICES = (
                        ('lsu','Lean Startt up '),
                        ('mod','Modelo de Negócios'),
                        ('des','Designer Thinking'),
                        ('out','Outras ?'), # pensar num if aqui 
            )
    sua_startup_possui_conhecimento_ou_e_treinada_nas_metodologias_descritas_abaixo = MultiSelectField(choices=possui_CHOICES,default=0)
    caso_outra = models.CharField(max_length=100,blank=True)

    ##################################################################################

    startup_foi_fundada_dentro_dos_5_anos_de_graduacao_dos_fundadores = models.BooleanField(default=0,choices = sim_nao_CHOICES)

    numero_de_socios =   models.CharField(max_length = 1000)
    ano_de_fundacao  =   models.CharField(max_length = 4)

    ja_foi_investida =   models.BooleanField(choices=sim_nao_CHOICES,default=0)
    quantas_rodadas  =   models.CharField(max_length = 10000)

    montante_investido = models.CharField(max_length = 1000000000)


    receita_CHOICES = ( 
                        receita_lazy() 
                    )
    quais_os_modelos_de_receitas_se_enquadra_no_perfil_da_empresa_startup = models.CharField(max_length = 3,choices=receita_CHOICES,default=0)
    quais_programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_participa = models.TextField()
    com_quais_entidades_do_ecossistema_tem_conexao_interacao_frequente_projetos_em_parceria_colaboracao_que_contribuiram_e_contribuem_para_as_inovacoes_e_aperfeicoamento_da_empresa = models.TextField()

    esfera_CHOICES = (
                        ("reg",'Regional'),
                        ("est",'Estadual'),
                        ('nac','Nacional'),
                        ('int','Internacional'),
    )
    estes_parceiros_listados_acima_possuem_que_esfera = MultiSelectField(choices=esfera_CHOICES,default=0)


    

    
    





    def __str__(self):
        return self.nome

    class Meta: 
        verbose_name_plural = "Dados_Mapeamento"

                                              

        



