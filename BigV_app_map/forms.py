from django.forms import ModelForm,Textarea
from django import forms
from BigV_app_map.models import Dados_Mapeamento_startup,Dados_Mapeamento_empresa
from django.forms.widgets import TextInput,RadioSelect,CheckboxSelectMultiple,FileInput,HiddenInput,Select

from phonenumber_field.widgets import PhoneNumberPrefixWidget

class TransacaoForm_Dados_startup(ModelForm):
    class Meta:
        model = Dados_Mapeamento_startup
        fields = '__all__'
                #     #Dados Cadastrais
                #     'nome','site','email','cnpj',
                #     #Endereço
                #    'cep','rua','bairro','cidade','estado',
                #     #Dados do Representante
                #    'nome_representante','cargo','telefone','email_representante', 
                #     #Característica da Empresa/Startup
                #    'setor_de_atuacao', 'area_de_atuacao_da_empresa_ou_startup','segmento_area','detalhes_de_area_de_atuacao','segmento_de_atuacao', 'tipo_de_cliente',
                #    #questionario 
                #    'possui_mercado_Global','possui_Influencia_ou_interesse_militar', 'qual_estrategia_de_saida_ou_idealizada_para_o_negocio',
                #    ]
                    #  
                
                
        #validar CNPJ e Email
        widgets = {
            #Dados Cadastrais
            'nome':  TextInput(attrs={'placeholder': 'Nome da Startup'}),
            'cnpj':  TextInput(attrs={'placeholder': ' xx.xxx.xxx/xxxx-xx'}),
            'site':  TextInput(attrs={'placeholder': 'http://www.seuwebsite.com'}),
            'email': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),
            'logo':  FileInput(attrs={'class':'label'}),
            #Endereço
            'cep': TextInput(attrs={'placeholder': 'xxxxx-xxx'}), ####### fazer Auto preenchimento com CEP
            
            #dados representante
            'telefone': PhoneNumberPrefixWidget(attrs={'placeholder': 'xxxxxxx-xxxx'}), ## arrumar aqui depois 
            
            'email_representante': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),
            
            
            #caracteristicas da startup
            'setor_de_atuacao': CheckboxSelectMultiple(), #arrumar depois as tag

            #Questionário
            'qual_estrategia_de_saida_ou_idealizada_para_o_negocio': CheckboxSelectMultiple(), #arrumar depois as tag
            'sua_startup_possui_conhecimento_ou_e_treinada_nas_metodologias_descritas_abaixo': CheckboxSelectMultiple(), #arrumar depois as tag
            
            'quais_programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_participa': Textarea(attrs={'id': 'Textarea'}),
            'com_quais_entidades_do_ecossistema_tem_conexao_interacao_frequente_projetos_em_parceria_colaboracao_que_contribuiram_e_contribuem_para_as_inovacoes_e_aperfeicoamento_da_empresa':Textarea(attrs={'id': 'Textarea'}),
            
            
        }

class TransacaoForm_Dados_empresa(ModelForm):
    class Meta:
        model = Dados_Mapeamento_empresa
        fields = '__all__'
        
        widgets = {
            
            ##Dados cadastrais
            'nome':    TextInput(attrs={'placeholder': 'Nome da Empresa'}),
            'pessoas': CheckboxSelectMultiple(),
            'logo':    FileInput(attrs={'class':'label'}),
            
            
            #Endereço institucional 
            'cep': TextInput(attrs={'placeholder': 'xxxxx-xxx'}), ####### fazer Auto preenchimento com CEP
            'site':  TextInput(attrs={'placeholder': 'http://www.seuwebsite.com'}),
            'email': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),

            #Dados do Representante
            'telefone': PhoneNumberPrefixWidget(attrs={'placeholder': 'xxxxxxx-xxxx'}), ## arrumar aqui depois 
            'email_representante': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),
            
            #Campo de Abrangência da Instituição Cadastrada
            'em_qual_destes_itens_abaixo_seu_cadastro_se_enquadra' : CheckboxSelectMultiple(),
            'em_qual_destes_setores_a_instituicao_se_enquadra' : Select(attrs={ 'onchange':"sumir(this.value);"}), #pegando função do js
    
            
            
            
            #Sobre Projetos, Iniciativas, parcerias e infraestrutura :
            'programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_executa' : Textarea(attrs={'id': 'Textarea'}),
            'programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_participa': Textarea(attrs={'id': 'Textarea'}),
            'equipamentos_disponiveis_para_uso_compartilhado_prestacao_de_servico_no_Ecossistema_Regional': Textarea(attrs={'id': 'Textarea'}),
            
            
            
            
        }