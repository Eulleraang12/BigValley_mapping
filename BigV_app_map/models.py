from django.conf import settings
from django.db import models
from localflavor.br.models  import BRCNPJField, BRPostalCodeField, BRStateField
from phonenumber_field.modelfields import PhoneNumberField
from .func_lazy import *
from multiselectfield import MultiSelectField #salvou minha vida 

class Dados_Mapeamento_startup(models.Model):
#dados cadastrais
    
    nome = models.CharField(max_length=100) # unique= True
    site = models.URLField(max_length=400, blank=True) 
    email = models.EmailField() 
    cnpj = BRCNPJField(null=True,blank=True) #fazer validação cnpj com js ou jquery
    logo = models.ImageField(upload_to='BigV_app_map/static/media_root',null=True,blank=True) 
########################################################################################################################################

#endereço
    cep = BRPostalCodeField(max_length=9, default='')           #fazer preenchimento automatico 
    rua = models.CharField(max_length=100, default='')
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')       #fazer como baixa de rolagem                                  
    estado = BRStateField()
# ########################################################################################################################################

# #dados do Representante 
    nome_representante = models.CharField(max_length=100, default='')
    cargo = models.CharField(max_length = 20, default='')
    telefone = PhoneNumberField(default='')
    email_representante = models.EmailField(default='')
# ########################################################################################################################################

# # Características da startup


    setor_de_atuaca_CHOICES = (
        ("ind", 'Indústria'),
        ("com", 'Comércio'),
        ("ser", 'Serviços'),
    )

    setor_de_atuacao = MultiSelectField(choices = setor_de_atuaca_CHOICES)

#     ##################################################################################

    area_de_atuacao_da_startup = models.CharField(max_length = 1000, default='')
    ##################################################################################
    segArea_CHOICES = ( 
                        seg_area_lazy() 
    
                    )

    segmento_area = models.CharField(max_length=100, choices = segArea_CHOICES,default='')
    ##################################################################################

    detalhes_de_area_de_atuacao = models.CharField(max_length = 1000, default='')

    ##################################################################################
    segAtu_CHOICES = ( 
                        seg_atu_lazy() 
                    )

    segmento_de_atuacao = models.CharField(max_length=100, choices = segAtu_CHOICES,default='')
    ##################################################################################
    tipoCliente_CHOICES = (
        ('B2B', 'Empresas e Negócios (B2B) '),
        ('B2C', 'Consumidores (B2C)'),
        ('GOV', 'Governo'),
    )
    tipo_de_cliente = models.CharField(max_length=100, choices = tipoCliente_CHOICES,default='')

# ########################################################################################################################################


#Questionário 
    sim_nao_CHOICES1 = ((True, 'Sim'), (False, 'Não'))
    sim_nao_CHOICES2 = ((True, 'Sim'), (False, 'Não'))
    sim_nao_CHOICES3 = ((True, 'Sim'), (False, 'Não'))
    sim_nao_CHOICES4 = ((True, 'Sim'), (False, 'Não'))
    

    possui_mercado_global = models.BooleanField(choices = sim_nao_CHOICES1,default=True)

    possui_Influencia_ou_interesse_militar =  models.BooleanField(choices = sim_nao_CHOICES2,default=True)
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
                        ('lsu','Lean Start up '),
                        ('mod','Modelo de Negócios'),
                        ('des','Designer Thinking'),
                        ('out','Outras ?'), # pensar num if aqui 
            )
    sua_startup_possui_conhecimento_ou_e_treinada_nas_metodologias_descritas_abaixo = MultiSelectField(choices=possui_CHOICES,default=0)
    caso_outra = models.CharField(max_length=100,blank=True,null=True)

    ##################################################################################

    startup_foi_fundada_dentro_dos_5_anos_de_graduacao_dos_fundadores = models.BooleanField(choices = sim_nao_CHOICES3,default=True)

    numero_de_socios =   models.CharField(max_length = 255, default='')
    ano_de_fundacao  =   models.CharField(max_length = 4, default='')

    ja_foi_investida =   models.BooleanField(choices=sim_nao_CHOICES4, default=True)
    quantas_rodadas  =   models.CharField(max_length = 255, default='') ##botar numeros 

    montante_investido = models.CharField(max_length = 255, default='')


    receita_CHOICES = ( 
                        receita_lazy() 
                    )
    quais_os_modelos_de_receitas_se_enquadra_no_perfil_da_empresa_startup = models.CharField(max_length = 100000,choices=receita_CHOICES,default='')
    quais_programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_participa = models.TextField(max_length = 100000, default='')
    com_quais_entidades_do_ecossistema_tem_conexao_interacao_frequente_projetos_em_parceria_colaboracao_que_contribuiram_e_contribuem_para_as_inovacoes_e_aperfeicoamento_da_empresa = models.TextField(max_length = 100000,default='')

    esfera_CHOICES = (
                        ("reg",'Regional'),
                        ("est",'Estadual'),
                        ('nac','Nacional'),
                        ('int','Internacional'),
    )
    estes_parceiros_listados_acima_possuem_que_esfera = MultiSelectField(choices=esfera_CHOICES, default=0)

    def __str__(self):
        return self.nome

    class Meta: 
        verbose_name_plural = "Dados_Mapeamento_Startup"




class Dados_Mapeamento_empresa(models.Model):
    
    nome = models.CharField(max_length=10)
    #Dados Cadastrias   ######################################
    pessoas_choices = (
                        ("PF","Pessoa Física"),
                        ("PJ","Pessoa Jurídica"),
    )
    pessoa = models.CharField(max_length=100, choices=pessoas_choices, default='')
    logo = models.ImageField(upload_to='BigV_app_map/static/media_root',null=True,blank=True) 
    
    #endereço institucional ######################################

    cep = BRPostalCodeField(max_length=9, default='')           #fazer preenchimento automatico 
    rua = models.CharField(max_length=100, default='')
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')       #fazer como baixa de rolagem                                  
    estado = BRStateField(default='')
    site = models.URLField(max_length=400, blank=True) 
    email = models.EmailField(default='') 
    #Dados do representante ######################################
    
    nome_representante = models.CharField(max_length=100, default='')
    cargo = models.CharField(max_length = 20, default='')
    telefone = PhoneNumberField(default='')
    email_representante = models.EmailField(default='')
    #Campo de Abrangência da Instituição Cadastrada ######################################
    
    itens_choices = (
                    ('aca','Academia (inst. de Nível Técnico ou Superior)'),
                    ('empre','Empresa'),
                    ('soc','Sociedade'),
                    ('gov','Governo'),                              
    )
    em_qual_destes_itens_abaixo_seu_cadastro_se_enquadra = MultiSelectField(choices = itens_choices, default=0)

    setores_choices = ( 
                    ('pol','Política'),
                    ('cul','Cultura'),
                    ('ch','Capital Humano'),
                    ('fin','Financeiro'),
                    ('sup','Suporte'),
                    ('merc','Mercado'),
)
    em_qual_destes_setores_a_instituicao_se_enquadra = models.CharField(max_length=100,choices = setores_choices, null=True)
    segmento_choices = ( 
                        seg_atu_lazy()
                        )
    ##Politica##
    ref_choices = (
        ('gov','Gorverno'),
        ('out','Outras Lideranças Política'),
    )
    sobre_referencia_politica = models.CharField(max_length=100,choices = ref_choices, default='',null=True,blank=True)
    #################################opções########################################################
    ## Cultura ##
    refcul_choices = (
        ('cul','Cultura / Valores Sociais e Empreendedores'),
    )
    referente_a_cultura = models.CharField(max_length=100,choices = refcul_choices,null=True,blank=True)
    
    ## Capital Humano ##
    refch_choices = ( 
                capital_humano_lazy() 
            )
    
    referente_a_capital_humano = models.CharField(max_length=100,choices = refch_choices,null=True,blank=True)
    
    ## Financeiro ##
    reffin_choices = (
        ('fin','Capital'),
    )
    referente_a_financeiro = models.CharField(max_length=100,choices = reffin_choices,null=True,blank=True)
    
    ## Suportee ##
    
    refsup_choices = ( 
                suporte_lazy()
            )
    
    referente_a_suporte = models.CharField(max_length=100,choices = refsup_choices,null=True,blank=True)
    
    ## Mercado ##
    
    ## não tem nada, perguntar pro samuel 
    # refmerc_choices  = (
        
    # )
    # referente_a_mercado = models.CharField(max_length=100,choices = refsup_choices,null=True,blank=True)
    
    
    
    
    refch_choices = ( 
                        seg_atu_lazy()
                    )
    segmento = models.CharField(max_length=100,choices = refch_choices, default='')


################################################################################################################

    #Sobre Projetos, Iniciativas, parcerias e infraestrutura ######################################
    programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_executa = models.TextField(max_length = 100000, default='')
    programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_participa = models.TextField(max_length = 100000, default='')
    equipamentos_disponiveis_para_uso_compartilhado_prestacao_de_servico_no_Ecossistema_Regional = models.TextField(max_length = 100000, default='')
    


    def __str__(self):
        return self.nome

    class Meta: 
        verbose_name_plural = "Dados_Mapeamento_Empresa"