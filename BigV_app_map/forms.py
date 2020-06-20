from django.forms import ModelForm
from django import forms
from BigV_app_map.models import Dados_Mapeamento
from django.forms.widgets import TextInput,RadioSelect,CheckboxSelectMultiple

class TransacaoForm_Dados(ModelForm):
    class Meta:
        model = Dados_Mapeamento
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
            'nome':  TextInput(attrs={'placeholder': 'Nome da Startup'}),
            'cnpj':  TextInput(attrs={'placeholder': ' xx.xxx.xxx/xxxx-xx'}),
            'site':  TextInput(attrs={'placeholder': 'http://www.seuwebsite.com'}),
            'email': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),

            'cep': TextInput(attrs={'placeholder': 'xxxxx-xxx'}), ####### fazer Auto preenchimento com CEP
            
            'telefone': TextInput(attrs={'placeholder': 'xxxxxxx-xxxx'}),
            

            'setor_de_atuacao': CheckboxSelectMultiple(),

            'possui_mercado_Global': RadioSelect(),
            'possui_Influencia_ou_interesse_militar': RadioSelect(),
            'qual_estrategia_de_saida_ou_idealizada_para_o_negocio': CheckboxSelectMultiple(),
            'sua_startup_possui_conhecimento_ou_e_treinada_nas_metodologias_descritas_abaixo':CheckboxSelectMultiple(),
            'startup_foi_fundada_dentro_dos_5_anos_de_graduacao_dos_fundadores': RadioSelect(),
            
            }



    
    
